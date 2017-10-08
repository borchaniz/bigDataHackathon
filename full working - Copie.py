
# coding: utf-8

# In[700]:

# LEL

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re


# In[701]:


# Importing dataset
dataset = pd.read_excel('ss.xlsx')[['type','post_message','post_published']]
dataset = dataset[dataset['type']=='status']
dataset['post_message'] = dataset['post_message'].str.lower()
dataset = dataset.drop('type',axis=1)
city = ['tunis','sfax']
dataset = dataset.dropna()
N=dataset.shape[0]


# In[702]:

#Adding type
dataset['type']= dataset['post_message'].apply(lambda x : '1' if 'dispo' in x.lower()  else '0')
dataset


# In[703]:

from datetime import datetime
from dateutil.parser import parse
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
mmap = {1: 'Jan',2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12 : 'Dec'}
#Formatting the date
dataset['date']= dataset['post_published'].apply(lambda war_start : datetime.strptime(war_start, "%Y-%m-%dT%H:%M:%S+%f"))
dataset['Hour'] = dataset['date'].apply(lambda time: time.hour)
dataset['Year'] = dataset['date'].apply(lambda time: time.year)
dataset['Month'] = dataset['date'].apply(lambda time: time.month)
dataset['Day'] = dataset['date'].apply(lambda time: time.day)
dataset['Day of Week'] = dataset['date'].apply(lambda time: time.dayofweek)
dataset['Month']= dataset['Month'].map(mmap)


# In[704]:

#Fixing The hour
p = re.compile('.*(\d\d)[\s]?h.*')
hours = [p.findall(dataset.iloc[i][0]) for i in range(0,N)]
hours = list(map(lambda x : -1 if len(x) == 0 else int(x[0]),hours))
p = re.compile('.*(\d)[\s]?h.*')
for i in range(0,N):
    if (hours[i] == -1):
        hour = p.findall(dataset.iloc[i][0])
        if(len(hour) != 0):
            hours[i] = hour[0]
p = re.compile('.*(\d\d):\d\d.*')
for i in range(0,N):
    if (hours[i] == -1):
        hour = p.findall(dataset.iloc[i][0])
        if(len(hour) != 0):
            hours[i] = hour[0]
p = re.compile('.*(\d):\d\d.*')
for i in range(0,N):
    if (hours[i] == -1):
        hour = p.findall(dataset.iloc[i][0])
        if(len(hour) != 0):
            hours[i] = hour[0]
for i in range(0,N):
    if hours[i] == -1 or not (0<=int(hours[i])<=23):
        hours[i] = dataset.iloc[i][2]
dataset['Hour'] = hours


# In[705]:

dataset=dataset.drop('post_published',1)


# In[706]:

# Number of places
p = re.compile(".*(\d).place.")
nb_places = [p.findall(dataset.iloc[i][0]) for i in range(0,N)]
nb_places = list(map(lambda x : 0 if len(x) == 0 else int(x[0]),nb_places))
n = ["une","deux","trois","quatre"]
for i in range(0,4):
    p = re.compile(".*"+n[i]+".place.")
    for j in range(0,N):
        if (len(p.findall(dataset.iloc[j][0])) != 0 and nb_places[j] == 0):
            nb_places[j] = i+1
dataset['n_places']=nb_places


# In[707]:

# Destinations
destinations = []
for i in range(0,N):
    if(city[0] in dataset.iloc[i][0] and city[1] in dataset.iloc[i][0]):
        if(dataset.iloc[i][0].index(city[0])<dataset.iloc[i][0].index(city[1])):
            destinations.append(1)
        else:
            destinations.append(0)
    else:
        destinations.append(-1)
dataset['destinations'] = destinations


# In[708]:

dataset=dataset.drop('post_message',1)


# In[709]:

dataset.to_excel('donnees.xlsx')

