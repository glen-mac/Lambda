import os
import glob
import pandas as pd
import numpy as np
import pickle

import matplotlib
import matplotlib.pyplot as plt

import seaborn as sns

from math import sqrt
from sklearn.linear_model import Ridge, RANSACRegressor
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.cross_validation import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.cluster import KMeans

def train_test_measure_reg(df, model, l_col, f_cols, scale_f=False, poly_f=False, picklize=False, save_dir="/"):
    """
    In: df        - DataFrame object that we want to learn from
        model     - sklearn ML object
        l_col     - label column name
        f_cols    - list of feature column names

    Out: tuple of mse and pred-true pairing DataFrame
    """

    X = df[f_cols].values
    y = df[l_col].tolist()

    X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.7, random_state=42)


    if poly_f:
        X_train, X_test = _transform(X_train, X_test, PolynomialFeatures())

    if scale_f:
        X_train, X_test = _transform(X_train, X_test, StandardScaler())

    reg = model
    reg.fit(X_train, y_train)

    if picklize:
        pickle.dump(reg, open(save_dir + "reg_model.p", "wb"))


    pred = reg.predict(X_test)


    pred_df = pd.DataFrame(data = {'pred': pred, 'true': y_test}, columns = ['pred', 'true'])
    mse = mean_squared_error(y_test, pred)
    return sqrt(mse), pred_df


def train_cl(df, model, f_cols, picklize=False, save_dir="/"):
    """
    In: df        - DataFrame object that we want to learn from
        model     - sklearn ML object
        l_col     - label column name
        f_cols    - list of feature column names
    Out: tuple of mse and pred-true pairing DataFrame
    """

    X = df[f_cols].values

    cl = model
    cl.fit(X)

    if picklize:
        pickle.dump(model, open(save_dir + 'cl_model.p', "wb"))

    pred = cl.predict(X)

    df['pred'] = pred

    return df


def _transform(X_train, X_test, transformer):
    tr = transformer.fit(X_train)

    X_train = tr.transform(X_train)
    X_test = tr.transform(X_test)

    return X_train, X_test


def predict(model, features):
    """
    IN:
    reg: sklearn prediction model (pickle file)
    features: feature column vector

    OUT: float of predicted tax deduction
    """
    preds = model.predict(features)
    return preds[0]

def load_model(path):
    """
    Loads pickle model for prediction stuff
    """
    return pickle.load(open(path, "rb"))

# Getting data

fname = os.path.join(os.path.dirname(__file__), '2014-15.txt') # change this to yoour path
df = pd.read_csv(fname, index_col=None, header=0)

# TODO: dummy variables: Occ_code, Partner_status, Region

reg_cols = ['Gender', 'age_range', 'Sw_amt']
cl_cols = ['Gender', 'age_range', 'Sw_amt']

# Training models

save_dir = os.path.join(os.path.dirname(__file__), 'models')

mse, pred_df = train_test_measure_reg(df=df,
                                      model=Ridge(),
                                      l_col='Tot_ded_amt',
                                      f_cols=reg_cols,
                                      scale_f=False,
                                      poly_f=False,
                                      picklize=True,
                                      save_dir=save_dir)

print "got regression model with mse = {}".format(mse)

cl_df = train_cl(df=df,
                 model=KMeans(),
                 f_cols=cl_cols,
                 picklize=True,
                 save_dir=save_dir)

print "got clustering model"

# Getting models

models_dir = os.path.join(os.path.dirname(__file__), 'models')

reg_model = load_model(models_dir + "reg_model.p")
print reg_model

cl_model = load_model(models_dir + "cl_model.p")
print cl_model

# Backend functions
def prediction_backend(vector):
    return predict(reg_model, vector)

def clustering_backend(vector):
    return predict(cl_model, vector)
