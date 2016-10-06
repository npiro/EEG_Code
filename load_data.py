# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 17:14:30 2016

@author: piromast
"""
import glob
from os.path import join
import scipy.io
import numpy as np

def load_trace(folder = '/Users/piromast/Documents/Kaggle/EEG/Data/train_1/', patient_index = 1, hour_index = 1, state = 'preictal'):
    """
    Loads a data trace corresponding to patient_index, at hour hour_index
    with specified state ('preictal' for seizure and 'normal' for normal)
    """
    if state == 'preictal': K = 1
    else: K = 0
    
    valid_indeces = range(1+(hour_index-1)*6,1+hour_index*6)
    
    get_subtrace_index = lambda name: int(name[len(folder)+2:-6])
    
    files = glob.glob(join(folder,str(patient_index)+'_*_'+str(K)+'.mat'))
    files = [f for f in files if get_subtrace_index(f) in valid_indeces]    
    
    sortedfiles = sorted(files, key=get_subtrace_index)
    print(sortedfiles)


    data = []
    for i, f in enumerate(sortedfiles):
        #if i > 5: break
        mat = scipy.io.loadmat(f)
        dataStruct=mat['dataStruct']
        data.extend(dataStruct['data'][0,0].tolist())
    
    data = np.array(data)
    return data
    
    