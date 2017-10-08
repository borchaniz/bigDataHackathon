

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import datetime

# In[711]:

fl = open('a.txt','w')
fl.write(':(*')
dataset=pd.read_excel('donnees.xlsx')


# In[712]:

# In[713]:
typevoy=1 # 1 offre
data_voy= dataset[dataset['type']==typevoy]


# In[ ]:




# In[ ]:
import dateutil.parser
inf = datetime.datetime.strptime(sys.argv[3] , "%Y-%m-%dT%H:%M")
inf += datetime.timedelta(days = 1)
sup = datetime.datetime.strptime(sys.argv[4] , "%Y-%m-%dT%H:%M")
sup += datetime.timedelta(days = 1)
if (sys.argv[1] == 'sf') & (sys.argv[2] == 'tn'):
    tunissfax = 0
else :
    tunissfax=1
sup = sup.replace(year=2016)
inf = inf.replace(year=2016)

if sys.argv[5] == 'cher':
    typevoy = "1"
else :
    typevoy = "0"
# typevoy = 1 if Offre

# In[714]:

#typevoy = 1 if Depart


# In[ ]:




# In[ ]:




# In[716]:

data_voy=data_voy.drop('type',1)


# In[718]:

data_2016 = data_voy[data_voy['Year']==2016]


# In[719]:

data_2016


# In[720]:

data_selected =data_2016[(data_2016['date'] <= sup) & (data_2016['date'] >= inf)]


# In[721]:

data_selected


# In[722]:

data_selected_dest = data_selected[data_selected['destinations']==tunissfax].drop(['destinations','Year','date'],1)
data_grouped = data_selected_dest.groupby(['Month','Day','Hour']).sum()


# In[723]:

#Search max
maxi = -1
indmaxi= 0
for index, row in data_grouped.iterrows() :
    if row['n_places'] > maxi :
        maxi=row['n_places']
        indmaxi=index

filename= "b.txt"
file = open(filename,"w")
file.write(str(indmaxi[2]))
file.close()

# In[727]:


# In[724]:

X=data_grouped.loc[indmaxi[0],indmaxi[1],indmaxi[2]]


# In[725]:

X=data_grouped.xs([indmaxi[0],indmaxi[1]]).reset_index(level=[0,1])
f= plt.figure(1)
X.plot(x='Hour',y='n_places',kind='line')

date = dateutil.parser.parse(str(indmaxi[1])+'-'+str(indmaxi[0])+'-2017 00:00:00')
date += datetime.timedelta(days = -1)
fl.write(str(date.month))
fl.close()
plt.title('Availabe places : '+str(date.day)+'/'+str(date.month)+'/2017',fontsize=14)
plt.ylabel('Number of places',fontsize=14)
plt.xlabel('Hour',fontsize=14)
plt.savefig('foo.png')

