# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 06:24:56 2022

@author: mayur
"""

import scipy
from scipy import stats
from scipy.stats import norm

#t-score of 95% confidence interval for sample size of 25
stats.t.ppf(0.975,24)     #df = n-1 = 24


#t-score of 96% confidence interval for sample size of 25
stats.t.ppf(0.98,24)     #df = n-1 = 24

#t-score of 99% confidence interval for sample size of 25
stats.t.ppf(0.995,24)     #df = n-1 = 24