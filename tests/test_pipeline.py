import json
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
import pytest
from src.data import NUM,CAT,DATE,TARGET,GROUP,FORBIDDEN,validate,split
from src.pipeline import build

@pytest.fixture
def toy():
    # Explicit synthetic fixture for software tests ONLY, not empirical results.
    n=120
    d=pd.DataFrame({c:np.arange(n,dtype=float)%7+1 for c in NUM})
    for c in CAT:
        d[c]=np.where(np.arange(n)%3==0,'a','b')
    d[DATE]=pd.date_range('2020-01-01',periods=n,freq='h').astype(str)
    d[GROUP]=np.repeat(np.arange(n//2),2)
    d[TARGET]=np.repeat(np.arange(n//2)%2,2)
    d.loc[0,NUM[0]]=np.nan
    return d

def test_schema_and_target(toy):
    validate(toy)
    with pytest.raises(ValueError): validate(toy.drop(columns=[GROUP]))
    toy.loc[0,TARGET]=2
    with pytest.raises(ValueError): validate(toy)

def test_missing_target_group_and_dates(toy):
    for c in [TARGET,GROUP,DATE]:
        bad=toy.copy(); bad.loc[0,c]=np.nan
        with pytest.raises(ValueError): validate(bad)

def test_group_independence(toy):
    tr,te=split(toy)
    assert not set(toy.iloc[tr][GROUP]) & set(toy.iloc[te][GROUP])
    assert set(tr)|set(te)==set(range(len(toy)))

@pytest.mark.parametrize('flow',['A','B'])
@pytest.mark.parametrize('algo',['tree','knn'])
def test_pipeline_unknown_nan_shape_and_persistence(toy,flow,algo,tmp_path):
    tr,te=split(toy); train=toy.iloc[tr]; test=toy.iloc[te].copy()
    for c in CAT: test[c]='never_seen'
    p=build(flow,algo); p.fit(train,train[TARGET])
    features=p['features'].transform(test)
    assert not set(FORBIDDEN)&set(features.columns)
    z=p[:-1].transform(test)
    assert np.isfinite(z.data if hasattr(z,'toarray') else z).all()
    pred=p.predict(test); assert pred.shape==(len(test),)
    path=tmp_path/'model.joblib'; joblib.dump(p,path)
    np.testing.assert_array_equal(pred,joblib.load(path).predict(test))

def test_forbidden_inputs_do_not_change_predictions(toy):
    p=build(); p.fit(toy,toy[TARGET]); altered=toy.copy()
    for c in FORBIDDEN: altered[c]='secret_outcome'
    np.testing.assert_array_equal(p.predict(toy),p.predict(altered))

def test_real_data_contract_if_available():
    from src.data import read_csv
    path=Path('data/raw/DataCoSupplyChainDataset.csv')
    if not path.exists(): pytest.skip('Real dataset absent; not evidence of real-data execution')
    d,_=read_csv(path); validate(d)
    tr,te=split(d)
    assert not set(d.iloc[tr][GROUP])&set(d.iloc[te][GROUP])

def test_smoke_runner_synthetic_only(toy,tmp_path,monkeypatch):
    # Exercises integration, explicitly separate from real dataset experiment.
    from src.run import run
    monkeypatch.chdir(tmp_path)
    toy.to_csv('toy.csv',index=False)
    pd.DataFrame({'FIELDS':toy.columns,'DESCRIPTION':['synthetic test only']*len(toy.columns)}).to_csv('description.csv',index=False)
    out=run({'data':'toy.csv','description':'description.csv','seed':42,'max_rows':None,'test_size':.2,'cv':2,'n_jobs':1})
    m=json.loads((out/'manifest.json').read_text(encoding='utf-8'))
    assert m['status']=='COMPLETED'
    assert len(pd.read_csv(out/'tables'/'comparison.csv'))==6

def test_train_only_imputation(toy):
    p=build('A','tree'); p.fit(toy,toy[TARGET])
    learned=p['preprocess'].named_transformers_['numeric']['impute'].statistics_.copy()
    np.testing.assert_allclose(learned,toy[NUM].median().to_numpy())
    holdout=toy.copy(); holdout[NUM]=999999.0
    p.predict(holdout)
    np.testing.assert_array_equal(learned,p['preprocess'].named_transformers_['numeric']['impute'].statistics_)

def test_cv_groups_do_not_overlap(toy):
    from sklearn.model_selection import StratifiedGroupKFold
    tr,_=split(toy); train=toy.iloc[tr]
    for a,b in StratifiedGroupKFold(3,shuffle=True,random_state=42).split(train,train[TARGET],train[GROUP]):
        assert not set(train.iloc[a][GROUP])&set(train.iloc[b][GROUP])

def test_protocol_repeatability(toy):
    from src.data import protocol_split
    cfg={'seed':42,'max_rows':80,'test_size':.2}
    a,tr,te=protocol_split(toy,cfg)
    b,x,y=protocol_split(toy,cfg)
    assert a.index.equals(b.index)
    np.testing.assert_array_equal(tr,x)
    np.testing.assert_array_equal(te,y)
    assert not set(a.iloc[tr][GROUP]) & set(a.iloc[te][GROUP])
    assert toy[toy[GROUP].isin(a[GROUP])].index.equals(a.index)


def test_order_metrics_equal_weights_and_mixed_labels(tmp_path):
    from src.evaluation import order_metrics
    d=pd.DataFrame({GROUP:[1,1,1,2],TARGET:[1,1,1,0]})
    path=tmp_path/'metrics.json'
    order_metrics(d,np.array([.9,.9,.9,.9]),path)
    result=json.loads(path.read_text())
    assert result['orders']==2 and result['accuracy']==.5
    assert result['confusion_matrix']==[[0,1],[0,1]]
    d.loc[0,TARGET]=0
    order_metrics(d,np.ones(4),path)
    assert json.loads(path.read_text())['status']=='BLOCKED'
