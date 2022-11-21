# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 18:22:40 2022

@author: mayur
"""

import numpy as np
import pandas as pd

df=pd.read_csv("Q7.csv")
df

#Mean
df.mean()

#Median
df.median()

#Mode
df.Points.mode()

df.Score.mode()

df.Weigh.mode()

#Variance

#Standard Deviation
df.std()

#Range
df.describe()

#Difference between maximum and minimun values

Points_Range=df.Points.max()-df.Points.min()
Points_Range

Score_Range=df.Score.max()-df.Score.min()
Score_Range

Weigh_Range=df.Weigh.max()-df.Weigh.min()
Weigh_Range


#Plots
import matplotlib.pyplot as plt

df['Weigh'].plot(kind='hist')

df['Points'].plot(kind='hist')
plt.plot(df['Points'])

df['Score'].plot(kind='hist')

df['Score'].plot(kind='hist',bins=5)

df['Score'].plot(kind='hist',bins=15)


plt.plot(df['Weigh'])


#Box Plot
f,ax=plt.subplots(figsize=(15,5))

plt.subplot(1,3,1)
plt.boxplot(df.Points)
plt.title('Points')

plt.subplot(1,3,2)
plt.boxplot(df.Score)
plt.title('Score')

plt.subplot(1,3,3)
plt.boxplot(df.Weigh)
plt.title('Weigh')

plt.show()


