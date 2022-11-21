# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 06:00:41 2022

@author: mayur
"""


import scipy
from scipy import stats
from scipy.stats import norm


#Z scores of 90% comfidence Interval
stats.norm.ppf(0.95)

#Z-scores of 94% Confidence Interval

#A 94 % confidence interval has two tails of 6/2 = 3, %so it goes from 3% to 97% which leaves 94% in the middle

stats.norm.ppf(0.97)

#Z-scores of 60% confidence Interval
stats.norm.ppf(0.8)