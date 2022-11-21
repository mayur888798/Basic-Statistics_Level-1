# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 23:08:47 2022

@author: mayur
"""

import numpy as np
import pandas as pd

import scipy
from scipy import stats
from scipy.stats import norm


#Average Weight of adult in Mexico with 94% CI
stats.norm.interval(0.94,200,30/(2000**0.5))


#Average weight of Adult Mexico with 96% CI
stats.norm.interval(0.96,200,30/(2000**0.5))


#Average weight of Adult in Mexico with 98% CI
stats.norm.interval(0.98,200,30/(2000**0.5))