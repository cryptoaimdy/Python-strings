#!/usr/bin/env python
# coding: utf-8

# In[1]:


# splitting string
text = 'blockchain is a plateform'
  
# Splits at space 
print(text.split()) 
  


# In[2]:


word = 'blockchain, is, a, plateform'
  
# Splits at ',' 
print(word.split(', ')) 
  


# In[3]:


word = 'blockchain: is: a: plateform'
  
# Splitting at ':' 
print(word.split(':')) 
  


# In[4]:


word = 'CatBatSatFatOr'
  
# Splitting at 3 
print([word[i:i+3] for i in range(0, len(word), 3)]) 


# In[ ]:




