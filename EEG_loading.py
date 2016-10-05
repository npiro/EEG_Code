
# coding: utf-8

# In[36]:

#get_ipython().magic('matplotlib inline')
import scipy.io
from os.path import join
import glob
from matplotlib.pyplot import *
import seaborn
import numpy as np
folderNico = '/Users/piromast/Documents/Kaggle/EEG/Data/train_1/'
folder = folderNico
files = glob.glob(join(folder,'1_*_1.mat'))


# In[37]:

sortedfiles = sorted(files, key=lambda name: int(name[len(folder)+2:-6]))


# In[39]:

data = []
for i, f in enumerate(sortedfiles):
    if i > 5: break
    mat = scipy.io.loadmat(f)
    dataStruct=mat['dataStruct']
    data.extend(dataStruct['data'][0,0].tolist())
    
data = np.array(data)


# In[40]:

plot(data[:,0])


# In[ ]:



