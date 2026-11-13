"""Generate honest notebooks without fabricated execution outputs."""
import json
from pathlib import Path
names = ['01_eda','02_preprocessing','03_model_experiments','04_error_analysis']
setup = '''from pathlib import Path
import os, sys
if not Path('src').is_dir(): os.chdir('..')
sys.path.insert(0, str(Path.cwd()))'''
codes = [
'''from src.data import read_csv, validate
from src.audit import audit, plots
from src.data import split
df, encoding = read_csv('data/raw/DataCoSupplyChainDataset.csv')
validate(df)
description, _ = read_csv('data/raw/DescriptionDataCoSupplyChain.csv')
print(df.shape, encoding)
print(df['Late_delivery_risk'].value_counts())
# Separate audit folder; plots on train only.
out = Path('results/notebook_eda')
audit(df, description, out)
tr, te = split(df)
plots(df.iloc[tr], out/'figures')''',
'''from src.data import read_csv, validate, split
from src.pipeline import build
df, _ = read_csv('data/raw/DataCoSupplyChainDataset.csv')
validate(df)
tr, te = split(df)
print('Group-safe split:', len(tr), len(te))
print(build('A', 'knn'))
print(build('B', 'tree'))''',
'''import json
from src.run import run
run(json.loads(Path('configs/default.json').read_text(encoding='utf-8-sig')))''',
'''import pandas as pd
runs = sorted(Path('results/runs').glob('*/summary_vi.md'))
if not runs: raise RuntimeError('NOT RUN: execute experiment first')
latest = runs[-1].parent
print((latest/'summary_vi.md').read_text(encoding='utf-8'))
display(pd.read_csv(latest/'tables/error_examples.csv'))'''
]
for name,code in zip(names,codes):
    cells=[{'cell_type':'markdown','metadata':{},'source':[f'# {name}\n','Outputs empty until executed. Uses reusable src modules; no invented metrics.']}]
    for source in [setup,code]:
        cells.append({'cell_type':'code','metadata':{},'execution_count':None,'outputs':[],'source':source.splitlines(True)})
    nb={'cells':cells,'metadata':{'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'}},'nbformat':4,'nbformat_minor':5}
    (Path('notebooks')/(name+'.ipynb')).write_text(json.dumps(nb,ensure_ascii=False,indent=2),encoding='utf-8')
