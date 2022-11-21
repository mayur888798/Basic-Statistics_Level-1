# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 03:22:03 2022

@author: mayur
"""

import numpy as np
import pandas as pd

df=pd.read_csv("Cars.csv")
df

df.head()

df.shape

df.describe()

import matplotlib.pyplot as plt

plt.boxplot(df)

import seaborn as sns

sns.boxplot(df.MPG)

import scipy
from scipy import stats
from scipy.stats import norm


# P (MPG>38)
1-stats.norm.cdf(38,df.MPG.mean(),df.MPG.std())


# P (MPG<40)
stats.norm.cdf(40,df.MPG.mean(),df.MPG.std())


# P (20<MPG<50)
stats.norm.cdf(0.50,df.MPG.mean(),df.MPG.std()-stats.norm.cdf(0.20,df.MPG.mean(),df.MPG.std()))