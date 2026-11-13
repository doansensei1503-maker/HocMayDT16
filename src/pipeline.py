import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.dummy import DummyClassifier
from .data import NUM, CAT, DATE

class SafeFeatures(BaseEstimator, TransformerMixin):
    def __init__(self, flow='A'):
        self.flow = flow
    def fit(self, X, y=None):
        if self.flow not in ['A','B']:
            raise ValueError('Unknown flow')
        return self
    def transform(self, X):
        out = X[NUM + CAT].copy()
        for col in CAT:
            out[col] = out[col].astype(object).where(out[col].notna(), np.nan)
        if self.flow == 'B':
            dt = pd.to_datetime(X[DATE], errors='raise')
            out['order_month'] = dt.dt.month
            out['order_weekday'] = dt.dt.dayofweek
            out['order_hour'] = dt.dt.hour
        return out

def build(flow='A', algorithm='tree', seed=42):
    nums = NUM + (['order_month','order_weekday','order_hour'] if flow == 'B' else [])
    pre = ColumnTransformer([
        ('numeric', Pipeline([('impute', SimpleImputer(strategy='median', keep_empty_features=True)), ('scale', StandardScaler())]), nums),
        ('categorical', Pipeline([('impute', SimpleImputer(strategy='most_frequent', keep_empty_features=True)), ('encode', OneHotEncoder(handle_unknown='ignore', sparse_output=True))]), CAT),
    ], sparse_threshold=1.0)
    model = {'tree':DecisionTreeClassifier(random_state=seed), 'knn':KNeighborsClassifier(algorithm='brute', n_jobs=1), 'dummy':DummyClassifier(strategy='most_frequent')}[algorithm]
    return Pipeline([('features',SafeFeatures(flow)),('preprocess',pre),('model',model)])

def grid(algorithm):
    if algorithm == 'knn':
        return {'model__n_neighbors':[5,15], 'model__weights':['uniform','distance'], 'model__metric':['euclidean','manhattan']}
    return {'model__max_depth':[4,10,None], 'model__min_samples_leaf':[5,20], 'model__criterion':['gini','entropy']}
