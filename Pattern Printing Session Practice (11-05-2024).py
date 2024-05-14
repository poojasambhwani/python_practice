#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(1,5):
    for j in range(1,5):
        print(i,end=" ")
    print(" ")


# In[2]:


for i in range(1,5):
    for j in range(1,5):
        print(j,end=" ")
    print(" ")


# In[11]:


for i in range(1,5):
    for j in range(4,0,-1):
        print(j,end=" ")
    print(" ")


# In[12]:


for i in range(1,4):
    for j in range(101,104):
        print(j,end=" ")
    print(" ")


# In[13]:


for i in range(1,5):
    for j in range(i):       #for j in range(1,i+1)
        print("*",end=" ")
    print(" ")


# In[26]:


for i in range(1,5):
    for j in range(i,5):    
        print("*",end=" ")
    print(" ")


# In[28]:


for i in range(1,5):
    for s in range(i,4):
        print("$",end=" ")
    for j in range(i):
        print("*",end=" ")
    print(" ")


# In[2]:


for i in range(1,5):
    for j in range(1,5):
        print("*",end=" ")
    print(" ")

