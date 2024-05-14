#!/usr/bin/env python
# coding: utf-8

# In[7]:


x=23
y=87
z=10
if(x<=y and x<=z):
    print("x is minimum")
elif(y<=x and y<=z):
    print("y is minimum")
elif(z<=x and z<=y):
    print("z is minimum")
else:
    print("Invalid input")


# In[23]:


a=86
if(a>=60 and a<75):
    print("average")
elif(a>=75 and a<85):
    print("good")
elif(a>=85 and a<95):
    print("excellent")
elif(a>=95 and a<100):
    print("brilliant")
else:
    print("fail")


# In[17]:


a=15
if(a%2==0 or a%3==0):
    print("A is divisible by 6")
else:
    print("Invalid input")


# In[18]:


a=6
if(a==1):
    print("January")
if(a==2):
    print("Febuary")
if(a==3):
    print("March")
if(a==4):
    print("April")
if(a==5):
    print("May")
if(a==6):
    print("June")
if(a==7):
    print("July")
if(a==8):
    print("August")
if(a==9):
    print("September")
if(a==10):
    print("October")
if(a==11):
    print("November")
if(a==12):
    print("December")


# In[16]:


x=100
total=0

if (x >= 10):
    total = 10*50
    x = x - 10
if (x >= 20):
    total = total + 20 * 20
    x = x - 20
if(x >= 10):
    total = total + 10*10
    x = x - 10
if(x >= 5):
    total = total+ x * 5

print("Total amount:", total)

