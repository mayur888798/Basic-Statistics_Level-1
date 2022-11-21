# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 22:05:22 2022

@author: mayur
"""

import numpy as np
import pandas as pd

df1=pd.read_csv("Q9_a.csv")
df1

#Skewness

df1.skew()

#Kurtosis

df1.kurt()



df2=pd.read_csv("Q9_b.csv")

#Skewness

df2.skew()

#Kurtosis

df2.kurt()