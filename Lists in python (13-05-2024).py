#!/usr/bin/env python
# coding: utf-8

# In[1]:


mylist=[10,20,"hello"]
mylist[-1]


# In[2]:


mylist=[10,20,"hello"]
mylist[0:3]


# In[8]:


mylist=[10,20,"hello"]
mylist[0]=6
print(mylist)


# In[9]:


x=mylist.pop(0)
print(mylist)
print(x)


# In[10]:


del mylist[-1]
print(mylist)


# In[11]:


help(mylist)


# In[24]:


l=[8,5,3,"good",2,"bad"]
sq_list = []
for i in l:
    if(type(i) is int):
        sq_list.append(i**2)
print(sq_list)


# In[31]:


s=["ram","jin","suga","jhope","jimin","vmin","jlk"]
add_list = []
for i in s:
    if(type(i) is str):
        add_list.append(i[0]+i[-1])
print(add_list)

