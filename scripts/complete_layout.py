from pathlib import Path
p=Path('scripts/finalize_evidence.py')
s=p.read_text(encoding='utf-8-sig')
s=s.replace('render(out)\nprint(out)', '''import shutil
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
shutil.copy2(out/'tables'/'split.csv','data/processed/split.csv')
render(out)
print(out)''')
p.write_text(s,encoding='utf-8')
