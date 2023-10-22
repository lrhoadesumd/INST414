#!/usr/bin/env python
# coding: utf-8

# In[186]:


import numpy
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


# In[167]:


df = pd.read_csv('top_10000_1960-now.csv')
selected_columns = ['Artist Name(s)', 'Tempo', 'Acousticness', 'Instrumentalness']
draft_data = df[selected_columns]
data1 = draft_data.dropna()
data= data1.reset_index()
data


# In[168]:


ts_songs= data[data['Artist Name(s)']=='Taylor Swift']
ts_tempo= ts_songs['Tempo'].values.reshape(-1,1)
all_temp=data['Tempo'].values.reshape(-1,1)


# In[169]:


scaler= StandardScaler()
taylor_tempo= scaler.fit_transform(ts_tempo)
all_tempo=scaler.transform(all_temp)


# In[171]:


similarity_scores = cosine_similarity(taylor_tempo, all_tempo)
data.loc[:,'Tempo Similarity'] = similarity_scores[0]
top_tempo_songs= data.sort_values(by= 'Tempo Similarity', ascending=False)
top_tempo_songs


# In[172]:


ts_inst= ts_songs['Instrumentalness'].values.reshape(-1,1)
all_inst=data['Instrumentalness'].values.reshape(-1,1)


# In[173]:


taylor_instrumentalness= scaler.fit_transform(ts_inst)
all_instrumentalness=scaler.transform(all_inst)


# In[175]:


similarity_scores2 = cosine_similarity(taylor_instrumentalness, all_instrumentalness)
data.loc[:,'Instrumentalness Similarity'] = similarity_scores2[0]
top_instrumentalness_songs= data.sort_values(by= 'Instrumentalness Similarity', ascending=False)
top_instrumentalness_songs


# In[176]:


ts_acous= ts_songs['Acousticness'].values.reshape(-1,1)
all_acous=data['Acousticness'].values.reshape(-1,1)


# In[177]:


taylor_acous= scaler.fit_transform(ts_acous)
all_acoust=scaler.transform(all_acous)


# In[179]:


similarity_scores3 = cosine_similarity(taylor_acous, all_acoust)
data.loc[:,'Acousticness Similarity'] = similarity_scores3[0]
top_acousticness_songs= data.sort_values(by= 'Acousticness Similarity', ascending=False)
top_acousticness_songs


# In[196]:


top_tempo_songs.head(10)


# In[197]:


top_instrumentalness_songs


# In[198]:


top_acousticness_songs.head(10)


# In[ ]:




