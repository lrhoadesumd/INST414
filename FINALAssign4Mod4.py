#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
from sklearn.cluster import MiniBatchKMeans
import matplotlib.pyplot as plt


# In[29]:


df= pd.read_csv('spotify_daily_charts_tracks.csv')
df


# In[30]:


selected_columns = ['artist_id','artist_name', 'danceability', 'energy']
draft_data = df[selected_columns]
data = draft_data.dropna()
data


# In[34]:


# cluster songs with high danceability and energy
model = MiniBatchKMeans(n_clusters=25, n_init=128, max_iter=2048, tol=0.5, reassignment_ratio=0.5, random_state=31337)
numeric_columns = data.select_dtypes(include=['number'])
model.fit(numeric_columns)


# In[35]:


cluster_df = pd.DataFrame(zip(df.index, model.labels_), columns=["artist name", "cluster"])


# In[36]:


cluster_df


# In[37]:


cluster_df["cluster"].value_counts()


# In[38]:


cluster_artist_df = pd.DataFrame({'artist_name': data['artist_name'], 'cluster': model.labels_})

# Group the data by cluster and aggregate artists
clustered_artists = cluster_artist_df.groupby('cluster')['artist_name'].unique()

# Print artists in each cluster
for cluster, artists in clustered_artists.items():
    print(f'Cluster {cluster}: {", ".join(artists)}')


# In[39]:


import matplotlib.pyplot as plt


# In[40]:


plt.figure(figsize=(10, 6))
clustered_artists.apply(len).plot(kind='bar')
plt.title('Number of Artists in Each Cluster')
plt.xlabel('Cluster')
plt.ylabel('Number of Artists')
plt.show()


# In[ ]:





# In[ ]:




