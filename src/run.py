import argparse
import json
import platform
from pathlib import Path
from datetime import datetime, timezone
from time import perf_counter
import importlib.metadata
import joblib
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV, StratifiedGroupKFold, cross_validate
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix, ConfusionMatrixDisplay, roc_auc_score, average_precision_score
from .data import read_csv, validate, sha256, TARGET, GROUP, NUM, CAT, protocol_split, SPLIT_PROTOCOL
from .pipeline import build, grid
from .audit import audit, plots

def metrics(y,p,prob):
    return {'accuracy':accuracy_score(y,p),'precision':precision_score(y,p,zero_division=0),'recall':recall_score(y,p,zero_division=0),'f1':f1_score(y,p,zero_division=0),'roc_auc':roc_auc_score(y,prob),'pr_auc':average_precision_score(y,prob)}

def run(cfg):
    df, encoding=read_csv(cfg['data']); validate(df)
    desc, desc_encoding=read_csv(cfg['description'])
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    out=Path('results/runs')/stamp
    for folder in ['tables','figures','models']:
        (out/folder).mkdir(parents=True,exist_ok=False)
    manifest={'status':'RUNNING','config':cfg,'source':'https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis','encoding':encoding,'description_encoding':desc_encoding,'data_sha256':sha256(cfg['data']),'description_sha256':sha256(cfg['description']),'python':platform.python_version(),'versions':{p:importlib.metadata.version(p) for p in ['numpy','pandas','scikit-learn','matplotlib','seaborn','joblib']}}
    manifest_path=out/'manifest.json'
    def persist():
        manifest_path.write_text(json.dumps(manifest,indent=2,ensure_ascii=False),encoding='utf-8')
    persist()
    try:
        quality=audit(df,desc,out)
        sampled,tr,te=protocol_split(df,cfg)
        manifest['split_protocol']=SPLIT_PROTOCOL
        from .evaluation import representativeness
        representativeness(df, sampled, out/'tables')
        train,test=sampled.iloc[tr],sampled.iloc[te]
        y=train[TARGET].astype(int); yt=test[TARGET].astype(int)
        manifest.update({'full_rows':len(df),'used_rows':len(sampled),'train_rows':len(train),'test_rows':len(test),'train_groups':train[GROUP].nunique(),'test_groups':test[GROUP].nunique(),'quality':quality,'metric_unit':'order-item','selection_metric':'CV F1 class 1; test never used for selection'})
        pd.DataFrame({'source_row':sampled.index,'partition':np.where(np.isin(np.arange(len(sampled)),tr),'train','test')}).to_csv(out/'tables'/'split.csv',index=False)
        plots(train,out/'figures')
        cv=list(StratifiedGroupKFold(n_splits=cfg['cv'],shuffle=True,random_state=cfg['seed']).split(train,y,train[GROUP]))
        for a,b in cv:
            assert not set(train.iloc[a][GROUP]) & set(train.iloc[b][GROUP])
            if y.iloc[a].nunique()!=2 or y.iloc[b].nunique()!=2:
                raise ValueError('CV fold lacks a class')
        scoring={'f1':'f1','recall':'recall','precision':'precision','accuracy':'accuracy'}
        candidates=[]
        for name,flow,algo in [('baseline_tree_A','A','tree'),('dummy_A','A','dummy')]+[(f'{a}_{f}',f,a) for f in ['A','B'] for a in ['knn','tree']]:
            pipe=build(flow,algo,cfg['seed']); start=perf_counter()
            if name.startswith('baseline') or algo=='dummy':
                scores=cross_validate(pipe,train,y,cv=cv,scoring=scoring,return_train_score=True,n_jobs=cfg['n_jobs'],error_score='raise')
                pipe.fit(train,y)
                c={f'cv_{m}':float(np.mean(scores['test_'+m])) for m in scoring}
                c['cv_f1_std']=float(np.std(scores['test_f1']))
                pd.DataFrame(scores).to_csv(out/'tables'/f'{name}_cv.csv',index=False)
                params=pipe['model'].get_params()
            else:
                search=GridSearchCV(pipe,grid(algo),scoring=scoring,refit='f1',cv=cv,n_jobs=cfg['n_jobs'],return_train_score=True,error_score='raise')
                search.fit(train,y); pipe=search.best_estimator_
                pd.DataFrame(search.cv_results_).to_csv(out/'tables'/f'{name}_cv.csv',index=False)
                c={f'cv_{m}':float(search.cv_results_['mean_test_'+m][search.best_index_]) for m in scoring}
                c['cv_f1_std']=float(search.cv_results_['std_test_f1'][search.best_index_]); params=search.best_params_
            c.update({'name':name,'flow':flow,'algorithm':algo,'search_and_refit_seconds':perf_counter()-start,'params':json.dumps(params,default=str)})
            candidates.append((pipe,c))
            print(f'FITTED {name}: CV F1={c["cv_f1"]:.4f}',flush=True)
        # Lock winner before any test predictions. All configurations were predeclared.
        winner=max(candidates,key=lambda x:x[1]['cv_f1'])[1]['name']
        manifest['selected_by_cv']=winner; persist()
        from .evaluation import time_ablation, order_metrics
        time_ablation(train, y, cv, candidates, cfg, out/'tables')
        rows=[]
        for pipe,c in candidates:
            start=perf_counter(); pt=pipe.predict(train); c['train_predict_seconds']=perf_counter()-start
            c['train_f1']=f1_score(y,pt,zero_division=0)
            start=perf_counter(); p=pipe.predict(test); prob=pipe.predict_proba(test)[:,1]; c['test_predict_and_probability_seconds']=perf_counter()-start
            c.update({'test_'+k:v for k,v in metrics(yt,p,prob).items()})
            order_metrics(test, prob, out/'tables'/f'{c["name"]}_order_metrics.json')
            c['train_minus_cv_f1']=c['train_f1']-c['cv_f1']; c['cv_minus_test_f1']=c['cv_f1']-c['test_f1']
            name=c['name']; rows.append(c)
            (out/'tables'/f'{name}_report.json').write_text(json.dumps(classification_report(yt,p,output_dict=True,zero_division=0),indent=2),encoding='utf-8')
            cm=confusion_matrix(yt,p,labels=[0,1]); pd.DataFrame(cm,index=['true_0','true_1'],columns=['pred_0','pred_1']).to_csv(out/'tables'/f'{name}_confusion.csv')
            ConfusionMatrixDisplay(cm,display_labels=[0,1]).plot(); plt.title(name); plt.tight_layout(); plt.savefig(out/'figures'/f'{name}_confusion.png'); plt.close()
            joblib.dump(pipe,out/'models'/f'{name}.joblib')
            restored=joblib.load(out/'models'/f'{name}.joblib'); np.testing.assert_array_equal(p,restored.predict(test))
            if name==winner:
                # No identifiers, names, addresses, timestamps or raw row indices.
                safe=test[NUM+['Shipping Mode','Customer Segment','Market','Order Region']].reset_index(drop=True)
                safe['true']=yt.to_numpy(); safe['predicted']=p
                safe['error']=np.where((yt.to_numpy()==1)&(p==0),'FN',np.where((yt.to_numpy()==0)&(p==1),'FP','correct'))
                safe[safe.error!='correct'].groupby('error',group_keys=False).head(10).to_csv(out/'tables'/'error_examples.csv',index=False)
                safe['fn']=(safe.error=='FN').astype(int); safe['fp']=(safe.error=='FP').astype(int)
                for col in ['Shipping Mode','Market','Order Region']:
                    agg=safe.groupby(col).agg(n=('true','size'),actual_positive=('true','sum'),fn=('fn','sum'),fp=('fp','sum'))
                    agg['fn_rate']=agg.fn/agg.actual_positive.replace(0,np.nan)
                    agg['fp_rate']=agg.fp/(agg.n-agg.actual_positive).replace(0,np.nan)
                    agg.to_csv(out/'tables'/f'errors_by_{col.replace(" ","_")}.csv')
        result=pd.DataFrame(rows); result.to_csv(out/'tables'/'comparison.csv',index=False)
        result.set_index('name')[['cv_f1','test_f1','test_recall','test_precision']].plot.bar(figsize=(11,5),ylim=(0,1)); plt.tight_layout(); plt.savefig(out/'figures'/'comparison.png'); plt.close()
        manifest['status']='COMPLETED'; persist()
        from .reporting import render
        render(out)
        print(f'COMPLETED {out}; selected_by_cv={winner}',flush=True)
        return out
    except Exception as exc:
        manifest.update(status='FAILED',error=repr(exc)); persist(); raise

def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--config',default='configs/default.json'); args=parser.parse_args()
    cfg=json.loads(Path(args.config).read_text(encoding='utf-8-sig')); run(cfg)
if __name__=='__main__':
    main()
