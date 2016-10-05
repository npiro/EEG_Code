
# coding: utf-8

# In[1]:

get_ipython().magic('matplotlib inline')
import scipy.io
from os.path import join
import glob
from matplotlib.pyplot import *
import seaborn
import numpy as np
folder = 'train_1/'
files = glob.glob(join(folder,'1_*_1.mat'))


# In[2]:

import re
pattern = '1_(\w+?)_1'
strings = ['1_16_1.mat','1_15_1.mat']
result = re.match(pattern, strings[0])
result.group()


# In[3]:

data = []
for i, f in enumerate(files):
    mat = scipy.io.loadmat(f)
    dataStruct=mat['dataStruct']
    data.extend(dataStruct['data'][0,0].tolist())
    if i >= 9: break
data = np.array(data)


# In[2]:

files


# In[6]:

data = dataStruct['data'][0,0]


# In[7]:

d = []
d.extend(data.tolist())
d.extend(data.tolist())
np.array(d).shape


# In[8]:

plot(data[:,10])


# In[ ]:



