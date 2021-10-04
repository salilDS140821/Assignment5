#!/usr/bin/env python
# coding: utf-8

# ## Write a Python class to implement pow(x, n)
# 
# 
# Explanation:
# 
# Use should be able to find the nth power of the x.(i.e x * x * x * x...n times)
# 
# You must implement it using Class
# 
# 
# Sample Input:
# 
# x: 10
# 
# n: 2
# 
# 
# Sample Output:
# 
# 100

# In[11]:


class Solution:
    
    def Power(x,n):
        
        return x**n


# In[12]:


Solution.Power(2,3)


# In[13]:


Solution.Power(4,3)


# In[18]:


Solution.Power(5,5)


# In[14]:


class Power:

    def find_power(x,n):

        return pow(x,n)

print(Power.find_power(2,3))


# In[15]:


Power.find_power(5,3)


# In[16]:


Power.find_power(6,4)


# In[17]:


Power.find_power(6,0)


# In[ ]:




