
# coding: utf-8

# In[1]:


print(reduce(lambda x,y:x*y,range(1,n+1)))


# In[8]:

from functools import reduce
def fat(n):
    return reduce(lambda x,y:x*y,range(1,n+1))


# In[9]:

fat(4)

