from pathlib import Path
import hashlib
import numpy as np
import pandas as pd
from sklearn.model_selection import GroupShuffleSplit

TARGET = 'Late_delivery_risk'
GROUP = 'Order Id'
DATE = 'order date (DateOrders)'
NUM = ['Days for shipment (scheduled)', 'Order Item Quantity', 'Order Item Product Price', 'Order Item Discount Rate']
CAT = ['Type', 'Shipping Mode', 'Customer Segment', 'Category Name', 'Department Name', 'Market', 'Order Region', 'Order Country', 'Order State']
FORBIDDEN = [TARGET, 'Delivery Status', 'Days for shipping (real)', 'Order Status', 'shipping date (DateOrders)', GROUP]
REQUIRED = NUM + CAT + [TARGET, GROUP, DATE]

def read_csv(path):
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(f'BLOCKED: missing {path}; see data/raw/README.md')
    for encoding in ['utf-8-sig', 'cp1252']:
        try:
            return pd.read_csv(path, encoding=encoding), encoding
        except UnicodeDecodeError:
            pass
    raise ValueError('Unsupported encoding; inspect file instead of replacing bytes')

def validate(df):
    if df.columns.duplicated().any():
        raise ValueError('Duplicate column names')
    missing = set(REQUIRED) - set(df.columns)
    if missing:
        raise ValueError(f'Missing required columns: {sorted(missing)}')
    if df[TARGET].isna().any() or set(df[TARGET].unique()) != {0, 1}:
        raise ValueError('Target must contain exactly numeric labels 0 and 1, without missing')
    if df[GROUP].isna().any():
        raise ValueError('Missing order group')
    for col in NUM:
        if not pd.api.types.is_numeric_dtype(df[col]) or np.isinf(df[col].dropna()).any():
            raise ValueError(f'Invalid numeric feature: {col}')
    if pd.to_datetime(df[DATE], errors='coerce').isna().any():
        raise ValueError('Missing/unparseable order date: explicit policy required')

def split(df, seed=42, test_size=.2):
    tr, te = next(GroupShuffleSplit(n_splits=1, test_size=test_size, random_state=seed).split(df, df[TARGET], df[GROUP]))
    if set(df.iloc[tr][GROUP]) & set(df.iloc[te][GROUP]):
        raise AssertionError('Order leakage')
    for idx in [tr, te]:
        if df.iloc[idx][TARGET].nunique() != 2:
            raise ValueError('Split has only one class; revise protocol before training')
    return tr, te

def subset_groups(df, limit, seed):
    if limit is None or len(df) <= limit:
        return df.copy()
    counts = df.groupby(GROUP, sort=False).size().sample(frac=1, random_state=seed)
    selected = counts[counts.cumsum() <= limit].index
    if len(selected) < 10:
        raise ValueError('Insufficient groups for requested sample budget')
    return df[df[GROUP].isin(selected)].copy()

def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

def feature_audit(df):
    rows = []
    for col in df:
        keep = col in NUM + CAT + [DATE]
        if col == TARGET:
            why = 'Target only; never input'
        elif col in ['Delivery Status','Days for shipping (real)','Order Status','shipping date (DateOrders)']:
            why = 'Outcome or post-order status; unavailable at prediction time'
        elif col == DATE:
            why = 'B only: calendar features; raw timestamp excluded'
        elif keep:
            why = 'Assumed available at order creation; verify operational contract'
        elif any(s in col.lower() for s in ['id','email','password','fname','lname','street','zipcode','image']):
            why = 'Identifier, personal information or high-cardinality proxy'
        else:
            why = 'Not allowlisted: timing/semantics uncertain or redundant; conservative exclusion'
        rows.append({'column':col,'decision':'keep' if keep else 'drop','reason':why,'certainty':'medium' if keep else 'high' if col in FORBIDDEN else 'medium'})
    return pd.DataFrame(rows)
