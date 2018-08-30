import numpy as np
import pandas as pd

def check_df_null(df):
    all_nulls = df.isnull().sum() / df.shape[0]
    all_nulls = all_nulls.loc[all_nulls != 0].sort_values(ascending = False)
    for i,v in all_nulls.iteritems():
        print('\'{:s}\' : {:0.2%}'.format(str(i), v))
    return all_nulls

def check_df_skew(df):
    cols = df.dtypes
    num_cols = cols[(cols == 'int64') | (cols == 'float64')].index.values.tolist()
    num_cols
    skews = df.apply(lambda x : x.skew() if x.name in num_cols else None )\
        .sort_values(ascending = False)
    return skews