# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 17:53:07 2016

@author: piromast
"""
# In[0]:
from matplotlib.pyplot import *
import pandas as pd

# In[1]:
dataNormal = load_trace(state='normal')
dataPreictal = load_trace(state='preictal')

# In[2]:

chan = [3]
ax = gca()
ax.clear()
avwin = 100
dfN = pd.DataFrame(dataNormal[:,:])
dfP = pd.DataFrame(dataPreictal[:,:])
plot(pd.rolling_mean(dfN.iloc[:100000,chan], avwin))
plot(pd.rolling_mean(dfP.iloc[:100000,chan], avwin))

# In[3]:
ax = gca()
ax.clear()
plot(dataNormal[:100000,chan],label='normal')
plot(dataPreictal[:100000,chan],label='preictal')
ax.legend()