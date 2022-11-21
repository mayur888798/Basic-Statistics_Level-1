# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 23:49:38 2022

@author: mayur
"""

import numpy as np
import pandas as pd

x=pd.Series([34,36,36,38,38,39,39,40,40,41,41,41,41,42,42,45,49,56])
x

#Mean
x.mean()

#Median
x.median()

#Variance
x.var()

#Standard Deviation
x.std()

#Histogram
x.plot(kind='hist')

x.plot(kind='hist',bins=15)
x.plot(kind='hist',bins=8)

import matplotlib.pyplot as plt
#Box Plot
plt.boxplot(x)

#there are two outliers (49, 56)