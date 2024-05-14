#!/usr/bin/env python
# coding: utf-8

# In[9]:


for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print(" ")


# In[14]:


count=1
for i in range(1,5):
    for j in range(1,i+1):
        print(count,end=" ")
        count=count+1
    print(" ")


# In[19]:


count=10
for i in range(1,5):
    for j in range(1,i+1):
        print(count,end=" ")
        count=count-1
    print(" ")


# In[3]:


for i in range(1,5):
    for j in range(65,65+i):
        print(chr(j),end=" ")
    print(" ")


# In[10]:


count=65
for i in range(1,5):
    for j in range(i):
        print(chr(count),end=" ")
        count=count+1
    print(" ")


# In[17]:


count=90
for i in range(1,4):
    for j in range(i):
        print(chr(count),end=" ")
        count=count-2
    print(" ")


# In[44]:


for i in range(1,6):
    for j in range(1,i+1):
        if j==1 or j==i or i==5:
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()


# In[54]:


count=1
alpha=65
for i in range(1,5):
    for j in range(i):
        print(count,end=" ")
        print(chr(alpha),end=" ")
        count=count+1
        alpha=alpha+1    
    print(" ")  


# In[105]:


count=1
for i in range(1,4):
    for s in range(i,5):
        print(count,end=" ")
        count=count+1
    for j in range(i):
        print("*",end=" ")
    print(" ")


# In[104]:


for i in range(1,5):
    alpha=1
    for s in range(4,i-1,-1):
        print(chr(64+alpha),end=" ")
        alpha=alpha+1
    for j in range(1,i+1):
        print(j,end=" ")
    print(" ")


# In[106]:


alpha=1
count=1
for i in range(1,5):
    for s in range(4,i-1,-1):
        print(chr(64+alpha),end=" ")
        alpha=alpha+1
    for j in range(1,i+1):
        print(count,end=" ")
        count=count+1
    print(" ")


# In[110]:


alpha=1
count=65
for i in range(1,5):
    for s in range(4,i,-1):
        print(" ",end=" ")
        alpha=alpha+1
    for j in range(i):
        print(chr(count),end=" ")
        count=count+1
    print(" ")


# In[144]:


for i in range(3):
    print(" " * i, end="")
    print("*" * (5 - 2 * i))

