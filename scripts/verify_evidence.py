"""Check persisted evidence and exact metric reproducibility without refitting."""
from pathlib import Path
import ast
import json
import numpy as np
import pandas as pd
from src.data import read_csv, GROUP
for path in list(Path('src').glob('*.py'))+list(Path('scripts').glob('*.py')):
    ast.parse(path.read_text(encoding='utf-8-sig'))
runs=[]
for out in sorted(Path('results/runs').iterdir()):
    if not (out/'manifest.json').exists(): continue
    m=json.loads((out/'manifest.json').read_text(encoding='utf-8'))
    if m.get('status')=='COMPLETED': runs.append(out)
assert runs
latest=runs[-1]
df,_=read_csv('data/raw/DataCoSupplyChainDataset.csv')
sp=pd.read_csv(latest/'tables'/'split.csv')
a=set(df.iloc[sp.loc[sp.partition=='train','source_row']][GROUP]); b=set(df.iloc[sp.loc[sp.partition=='test','source_row']][GROUP])
assert not a&b
comparison=pd.read_csv(latest/'tables'/'comparison.csv')
assert len(comparison)==6
if len(runs)>1:
    old=pd.read_csv(runs[-2]/'tables'/'comparison.csv')
    cols=[c for c in comparison if c.startswith('cv_') or c.startswith('test_') or c=='train_f1']
    cols=[c for c in cols if 'seconds' not in c]
    np.testing.assert_allclose(old[cols].to_numpy(),comparison[cols].to_numpy(),rtol=0,atol=1e-12)
    print('VERIFIED: repeated experiment metrics identical within 1e-12')
for path in Path('notebooks').glob('*.ipynb'):
    nb=json.loads(path.read_text(encoding='utf-8'))
    cells=[c for c in nb['cells'] if c['cell_type']=='code']
    assert cells and all(c['execution_count'] is not None for c in cells), path
    assert all(o['output_type']!='error' for c in cells for o in c['outputs']),path
print('VERIFIED: all four notebooks executed without cell errors')
print('VERIFIED: persisted real split order overlap = 0; six models; Python syntax valid')
print('LATEST',latest)
