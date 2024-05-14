#!/usr/bin/env python
# coding: utf-8

# In[1]:


ch=str(input("Enter a string: "))
count=0
for i in ch:
    count=count+1
print(count)


# In[2]:


v=str(input("Enter a string: "))
vowel=0
for j in v:
    if j in 'aeiouAEIOU':
        vowel=vowel+1
print(vowel)


# In[3]:


c=str(input("Enter a string: "))
const=0
for k in c:
    if k not in 'aeiouAEIOU':
        const=const+1
print(const)


# In[4]:


for i in range(99,4,-1):
    if(i%5==0 and i%7==0):
        print(i)


# In[12]:


pwd = input("Enter a password: ")
caps = 0
small = 0
num = 0
spcl = 0

if 5 <= len(pwd) <= 15:
    for i in pwd:
        if 'A' <= i <= 'Z':
            caps = caps + 1
        elif 'a' <= i <= 'z':
            small = small + 1
        elif '0' <= i <= '9':
            num = num + 1
        elif i in '@#&!':
            spcl = spcl + 1
    
    if caps >= 3 and small >= 2 and num >= 1 and spcl >= 1:
        print("Valid password")
    else:
        print("Invalid password")
else:
    print("Password length should be between 5 and 15 characters")

