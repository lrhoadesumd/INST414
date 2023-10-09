#!/usr/bin/env python
# coding: utf-8

# In[9]:


import wikipedia
import networkx as nx
import matplotlib.pyplot as plt
import requests
import numpy as np
import pandas as pd


# In[21]:


start_page_title= 'Taylor Alison Swift'
end_page_title = 'University of Maryland'


# In[22]:


G= nx.Graph()


# In[23]:


def add_links(page_title, depth=3):
    if depth > 3:
        return
    page= wikipedia.page(page_title)
    G.add_node(page.title)
    
    links=page.links

    for link in links: 
        G.add_edge(page.title, link)
        add_links(link, depth +1)


# In[24]:


add_links(start_page_title, depth = 3)
add_links(end_page_title, depth=3)


# In[25]:


pos = nx.spring_layout(G, scale=50, k=0.3)
nx.draw(G, 
        pos, 
        with_labels=True, 
        node_size=100, 
        node_color="pink", 
        font_size=10, 
        font_color="black")
plt.title("Connections Between Taylor Swift and The University of Maryland")
plt.show()


# In[27]:


taylorumd=nx.write_graphml(G, "taylorumd.graphml")
taylorumd


# In[ ]:




