"""Data audit; descriptive plots use train only after group split."""
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from .data import TARGET, GROUP, DATE, NUM, CAT, feature_audit

def audit(df, description, out):
    tables, figs = out/'tables', out/'figures'
    tables.mkdir(parents=True, exist_ok=True)
    figs.mkdir(parents=True, exist_ok=True)
    dictionary = pd.DataFrame({'column':df.columns, 'dtype':[str(df[c].dtype) for c in df], 'missing':[int(df[c].isna().sum()) for c in df], 'cardinality':[int(df[c].nunique()) for c in df]})
    if description.shape[1] < 2:
        raise ValueError('Description CSV requires field and description columns')
    mapping = dict(zip(description.iloc[:,0].astype(str).str.strip(), description.iloc[:,1].astype(str)))
    dictionary['source_description'] = dictionary['column'].map(mapping).fillna('NOT MATCHED: manual verification required')
    dictionary.to_csv(tables/'data_dictionary.csv',index=False)
    feature_audit(df).to_csv(tables/'feature_audit.csv',index=False)
    numeric = df.select_dtypes('number')
    numeric.describe().T.to_csv(tables/'numeric_summary.csv')
    rows=[]
    for col in numeric:
        q1,q3=numeric[col].quantile([.25,.75]); iqr=q3-q1
        rows.append({'column':col,'iqr_outliers':int(((numeric[col]<q1-1.5*iqr)|(numeric[col]>q3+1.5*iqr)).sum())})
    pd.DataFrame(rows).to_csv(tables/'outliers.csv',index=False)
    counts=df.groupby(GROUP).size()
    quality={'rows':len(df),'columns':len(df.columns),'duplicate_rows':int(df.duplicated().sum()),'orders':int(len(counts)),'repeated_order_rows':int(df[GROUP].duplicated().sum()),'orders_with_multiple_rows':int((counts>1).sum()),'mixed_label_orders':int((df.groupby(GROUP)[TARGET].nunique()>1).sum()),'class_counts':df[TARGET].value_counts().to_dict(),'policy':'No automatic removal of duplicates, missing values or outliers. Order-item weighting retained.'}
    (tables/'quality.json').write_text(json.dumps(quality,indent=2,ensure_ascii=False),encoding='utf-8')
    return quality

def plots(train, out):
    out.mkdir(parents=True,exist_ok=True)
    def save(name):
        plt.tight_layout(); plt.savefig(out/name,dpi=140); plt.close()
    train[TARGET].value_counts().sort_index().plot.bar(title='Train: target counts'); save('01_classes.png')
    train.isna().mean().sort_values(ascending=False).head(15).plot.bar(title='Train: missing fraction'); save('02_missing.png')
    train[NUM].hist(figsize=(10,7)); save('03_numeric_hist.png')
    sns.boxplot(data=train[NUM],orient='h'); plt.title('Train: original scales, no outlier removal'); save('04_boxplot.png')
    sns.countplot(data=train,x='Shipping Mode',hue=TARGET); plt.xticks(rotation=20); save('05_shipping.png')
    table=train.groupby('Order Region')[TARGET].agg(['mean','size']).sort_values('size',ascending=False)
    table['mean'].plot.bar(title='Train: late fraction by region (descriptive)'); save('06_regions.png')
    sns.heatmap(train[NUM].corr(),annot=True,vmin=-1,vmax=1); save('07_correlation.png')
    dates=pd.to_datetime(train[DATE]).dt.to_period('M').astype(str)
    train.groupby(dates)[TARGET].mean().plot(figsize=(10,4),title='Train: late fraction by order month'); save('08_month.png')
    table.to_csv(out.parent/'tables'/'train_region_support.csv')
