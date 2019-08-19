#!/usr/bin/env python
# coding: utf-8

# In[2]:


#string concatenation with + operator
s = 'a' + 'b' + 'c'
print(s)


# In[9]:


# strings are immutable when ever we concatenate a string with another we have to assign a new variale for them.

original_string = "hello"
original_string + "world"


# In[10]:


#this ll print only hello because we didnot stored concatenated string into a new variable.
print(original_string)


# In[11]:


# lets store concatenated string into a new variable.
new_string = original_string + "world"


# In[12]:


print(new_string)


# In[20]:


#Going From a List to a String in Python With .join

list_of_strings = ['a','b','c']
','.join(list_of_strings)


# In[13]:


# string multiplication. 

print (s*2)


# In[14]:



print(original_string*2)


# In[ ]:




