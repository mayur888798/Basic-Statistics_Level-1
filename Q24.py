# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 06:53:11 2022

@author: mayur
"""

from scipy import stats
from scipy.stats import norm

#Assme Null Hypothesis is Ho = Avg Life of Bulb is greater or equal to 260 days
#Alternate Hypothesis is Ha = Avg Life the Bulb is less than 260 days


#finding t-score at x=260; t=(s_mean-P_mean)/(s_SD/sqrt(n))
t=(260-270)/(90/18**0.5)
t

#Now find P(X is greater than or equal to 260) for null hypothesis

#Using cdf funtion
#p_value=1-stats.t.cdf(abs(t_scores),df=n-1)

p_value=1-stats.t.cdf(abs(-0.4714045),df=17)
p_value

#OR By using sf function
#p_value=stats.t.sf(abs(t_score),df=n-1)

p_value=stats.t.sf(abs(-0.4714045),df=17)
p_value