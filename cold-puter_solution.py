#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# ### Inputed number of temperature

# In[2]:


ilan = int(input())
neg = 0
temperatures = input().split()
for temp in temperatures:
    if int(temp) < 0:
        neg += 1
print (neg)


# ### Randomize Temperature

# In[3]:


ilan = int(input())
neg = 0
count = 0

while count < ilan:
    count += 1
    number = random.randrange(-1000000, 1000000)
    print(number,end=" ")
    if number < 0:
        neg = neg + 1
        
print("\n\nNumber of Negative Temperature: " + str(neg))


# ### Randomize All

# In[4]:


ilan = random.randrange(1, 100)
print("number of temperatures collected: " + str(ilan) + "\n")
neg = 0
count = 0

while count < ilan:
    count += 1
    number = random.randrange(-1000000, 1000000)
    print(number,end=" ")
    if number < 0:
        neg += 1
        
print("\n\nNumber of Negative Temperature: " + str(neg))


# In[ ]:




