import numpy as np
import pandas as pd
import pylab as plt
from scipy.stats import f_oneway,ttest_ind


def test1(df,col,group1,group2):
    filt = df['group']==group1
    g1 = df[filt].dropna()
    g1 = g1[col]
    filt = df['group']==group2
    g2 = df[filt].dropna()
    g2 = g2[col]
    pvalue = ttest_ind(g1,g2)[1]
    return pvalue

def test2(df,col):
    grps = []
    for grp_name in df['group'].unique():
        filt = df['group']==grp_name
        g = df[filt]
        g = g[col].dropna()
        grps.append(g)
    pvalue = f_oneway(*grps)[1]
    return pvalue


