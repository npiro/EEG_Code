
# coding: utf-8

# In[7]:

get_ipython().magic('matplotlib inline')
import scipy.io
from os.path import join
import glob
from matplotlib.pyplot import *
import seaborn
import numpy as np
folder = '/Users/piromast/Documents/Kaggle/EEG/Data/train_1/'
files = glob.glob(join(folder,'1_*_1.mat'))


# In[8]:

import re
pattern = '1_(\w+?)_1'
strings = ['1_16_1.mat','1_15_1.mat']
result = re.match(pattern, strings[0])
result.group()


# In[18]:

sortedfiles = sorted(files, key=lambda name: int(name[len(folder)+2:-6]))


# In[32]:

data = []
sequence = []
for i, f in enumerate(sortedfiles):
    if i > 5: break
    mat = scipy.io.loadmat(f)
    dataStruct=mat['dataStruct']
    data.extend(dataStruct['data'][0,0].tolist())
    sequence.extend(dataStruct['sequence'][0,0].tolist())
data = np.array(data)


# In[34]:

sortedfiles


# In[35]:
figure(0)
plot(data[:,:])


# In[ ]:



