from pandas import DataFrame
import numpy as np

"""
    desc: anomaly process module
    author:ywy
    date:2022-12-07
"""


def process_single_col_by_gauss(df: DataFrame, head, is_fill_nan=False):
    _mean = df[head].mean()
    _std = df[head].std()
    _up = _mean + (5*_std)
    _down = _mean - (5*_std)
    if is_fill_nan:
        df.loc[(df[head] >= _up), head] = np.nan
    else:
        df.loc[(df[head] >= _up), head] = _up
    return df, _up


def process_single_col_by_percentile(df: DataFrame, head, percent=0.95, is_fill_nan=False):
    _up = df[head].quantile(percent)
    if is_fill_nan:
        df.loc[(df[head] >= _up), head] = np.nan
    else:
        df.loc[(df[head] >= _up), head] = _up
    return df, _up


