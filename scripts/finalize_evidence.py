"""Supplement audit with business-label checks; never use these columns as features."""
from pathlib import Path
import json
import pandas as pd
import joblib
from sklearn.tree import export_text
from src.data import read_csv, TARGET, GROUP
from src.reporting import render
runs=sorted(p for p in Path('results/runs').glob('*')
            if (p/'summary_vi.md').exists() and (p/'manifest.json').exists()
            and json.loads((p/'manifest.json').read_text(encoding='utf-8')).get('status')=='COMPLETED')
if not runs:
    raise SystemExit('NOT RUN: execute python -m src.run before finalizing evidence')
out=runs[-1]
df,_=read_csv('data/raw/DataCoSupplyChainDataset.csv')
for col in ['Delivery Status','Order Status']:
    pd.crosstab(df[col],df[TARGET]).to_csv(out/'tables'/(col.replace(' ','_')+'_target_crosstab.csv'))
rows=[]
for col in ['Customer Id','Order Customer Id','Order Item Id']:
    rows.append({'column':col,'unique':df[col].nunique(),'duplicate_rows':int(df[col].duplicated().sum()),'missing':int(df[col].isna().sum())})
pd.DataFrame(rows).to_csv(out/'tables'/'related_group_audit.csv',index=False)
for col in ['Shipping Mode','Market','Order Region','Customer Segment']:
    df[col].value_counts(dropna=False).rename_axis('category').reset_index(name='count').to_csv(out/'tables'/('frequency_'+col.replace(' ','_')+'.csv'),index=False)
for name in ['baseline_tree_A','tree_A','tree_B']:
    p=joblib.load(out/'models'/(name+'.joblib'))
    names=p['preprocess'].get_feature_names_out()
    pd.DataFrame({'feature':names,'impurity_importance':p['model'].feature_importances_}).sort_values('impurity_importance',ascending=False).to_csv(out/'tables'/(name+'_importance.csv'),index=False)
    (out/'tables'/(name+'_rules.txt')).write_text(export_text(p['model'],feature_names=list(names),max_depth=4),encoding='utf-8')
import shutil
sp=pd.read_csv(out/'tables'/'split.csv')
train=df.iloc[sp.loc[sp.partition=='train','source_row']]
test=df.iloc[sp.loc[sp.partition=='test','source_row']]
overlaps=[]
for col in ['Order Id','Customer Id','Order Customer Id','Order Item Id','Product Card Id']:
    overlap=set(train[col])&set(test[col])
    overlaps.append({'column':col,'train_unique':train[col].nunique(),'test_unique':test[col].nunique(),'overlap_unique':len(overlap)})
pd.DataFrame(overlaps).to_csv(out/'tables'/'split_group_overlap_audit.csv',index=False)
m=json.loads((out/'manifest.json').read_text(encoding='utf-8'))
Path('results/models').mkdir(parents=True,exist_ok=True)
shutil.copy2(out/'models'/(m['selected_by_cv']+'.joblib'),'results/models/selected.joblib')
Path('data/processed').mkdir(parents=True,exist_ok=True)
shutil.copy2(out/'tables'/'split.csv','data/processed/split.csv')
render(out)
print(out)
print(pd.crosstab(df['Delivery Status'],df[TARGET]).to_string())
print(pd.read_csv(out/'tables'/'data_dictionary.csv').query('missing > 0')[['column','missing']].to_string(index=False))
