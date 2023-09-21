#!/usr/bin/env python
# coding: utf-8

# In[56]:


import requests
import numpy as np
import pandas as pd


# In[57]:


api_url = "http://ws.audioscrobbler.com/2.0/"
api_key = "fbc31c571aa9669c750bf368aff08f3c"


# In[58]:


params= {
    "method" : "artist.getTopTracks",
    "artist" : "Taylor Swift",
    "api_key" : api_key,
    "format" : "json"
}


# In[60]:


response = requests.get(api_url, params=params)

if response.status_code == 200:
    top_tracks = response.json().get("toptracks",{}).get("track",[])
    for rank,track in enumerate(top_tracks, start=1):
        title= track.get('name','')
        print(f"Rank {rank}: {title}")


# In[61]:


df = pd.DataFrame(top_tracks)
df = df[["name", "playcount", "listeners"]]


# In[62]:


df['playcount'] = pd.to_numeric(df["playcount"], errors = "coerce")
df['playcount'] = pd.to_numeric(df["listeners"], errors = "coerce")
df.dropna(inplace=True)


# In[63]:


df_summary = df[["name", "playcount", "listeners"]]
print(df_summary)


# In[72]:


df_summary.head(11)


# In[ ]:




