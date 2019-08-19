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


# In[17]:


#string TItle
#This function returns a string which has first letter in each word is uppercase and all remaining letters are lowercase.

name = "crypto aimdy"
print(str.title(name))


# In[18]:


#upper case, returns all character into upper case.

print(str.upper(name))


# In[19]:


#lower case, returns all character into lower case.

print(str.lower(name))


# In[20]:


#converts first character of string into upper case.
s = "i am python developer"

print(s.capitalize())


# In[ ]:




