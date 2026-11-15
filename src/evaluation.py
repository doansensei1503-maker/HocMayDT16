"""Aggregate diagnostics; historical holdout is never used for selection."""
import json
import numpy as np
import pandas as pd
from sklearn.model_selection import cross_validate
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from .data import GROUP, TARGET, CAT, NUM
from .pipeline import build


def representativeness(full, sampled, out):
    rows = []
    for col in [TARGET] + CAT:
        a = full[col].fillna('<missing>').value_counts(normalize=True)
        b = sampled[col].fillna('<missing>').value_counts(normalize=True)
        for category in a.index.union(b.index):
            rows.append(dict(column=col, category=category, full_fraction=a.get(category, 0),
                             subset_fraction=b.get(category, 0), difference=b.get(category, 0)-a.get(category, 0)))
    pd.DataFrame(rows).to_csv(out/'sampling_categories.csv', index=False)
    pd.DataFrame([dict(column=c, full_mean=full[c].mean(), subset_mean=sampled[c].mean(),
                       full_median=full[c].median(), subset_median=sampled[c].median()) for c in NUM]).to_csv(out/'sampling_numeric.csv', index=False)
    (out/'sampling_groups.json').write_text(json.dumps({name: dict(rows=len(d), orders=d[GROUP].nunique(),
        mean_items=d.groupby(GROUP).size().mean(), max_items=int(d.groupby(GROUP).size().max()))
        for name,d in [('full',full),('subset',sampled)]}, indent=2))


def order_metrics(test, probabilities, path):
    frame = pd.DataFrame({'group': test[GROUP].to_numpy(), 'y': test[TARGET].to_numpy(), 'p': probabilities})
    grouped = frame.groupby('group')
    if (grouped.y.nunique() > 1).any():
        path.write_text(json.dumps({'status': 'BLOCKED', 'reason': 'mixed target within order'}))
        return
    agg = grouped.agg(y=('y', 'first'), p=('p', 'mean'))
    y, p = agg.y, (agg.p >= .5).astype(int)
    result = {'status': 'COMPLETED', 'orders': len(agg), 'rule': 'mean row probability >= 0.5; equal order weights',
              'accuracy': accuracy_score(y,p), 'precision': precision_score(y,p,zero_division=0),
              'recall': recall_score(y,p,zero_division=0), 'f1': f1_score(y,p,zero_division=0),
              'confusion_matrix': confusion_matrix(y,p,labels=[0,1]).tolist()}
    path.write_text(json.dumps(result, indent=2))


def time_ablation(train, y, cv, candidates, cfg, out):
    rows = []
    for algorithm in ['knn', 'tree']:
        reference = next(pipe for pipe,c in candidates if c['name'] == algorithm+'_A')
        params = reference['model'].get_params()
        for flow in ['A', 'B']:
            pipe = build(flow, algorithm, cfg['seed'])
            pipe['model'].set_params(**params)
            scores = cross_validate(pipe, train, y, cv=cv, scoring={'f1':'f1','recall':'recall','precision':'precision','accuracy':'accuracy'},
                                    n_jobs=cfg['n_jobs'], error_score='raise')
            rows.append(dict(algorithm=algorithm, flow=flow, params=json.dumps(params, sort_keys=True),
                             **{k:float(np.mean(v)) for k,v in scores.items() if k.startswith('test_')}))
    pd.DataFrame(rows).to_csv(out/'time_ablation_cv.csv', index=False)
