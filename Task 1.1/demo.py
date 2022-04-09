#!/usr/bin/env python
# coding: utf-8

# # Name: Mohit Anand         Roll No. 190505
# ### Carscan 
# ### Assignment 1.1

# In[1]:


# Importing the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import cv2
import os
import random
from util import findxy, bbox


# In[3]:


opacity=0.5
pathway='E:/carscan_files/'
json_path='E:/carscan_files/'


# In[4]:


fig, ax = plt.subplots(nrows=5, ncols=1,figsize=(20,100))
a=1
for ee in range(1,6):
    image= os.path.join(pathway,str(ee)+'.jpg')
    json_data = os.path.join(json_path,str(ee)+'.json')
    output1 = bbox(image,json_data,opacity)
    fig.add_subplot(5, 1, a)
    plt.imshow(cv2.cvtColor(output1, cv2.COLOR_BGR2RGB))
    a=a+1


# In[ ]:




