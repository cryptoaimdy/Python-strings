#!/usr/bin/env python
# coding: utf-8

# In[11]:


#using strip to delete traiul and leading spaces


my_string = "    i am a developer and python is a good PL   "

#removes nothing
my_string.strip()


# In[14]:


#removes developer
my_string.strip("   PL")


# In[15]:


#removes nothing because spaces do not match
print(my_string.strip("developer"))


# In[21]:


#string count

my_string = "i am a developer and python is a good PL"
substring = "a"

my_string.count(substring)


# In[28]:


#string count after start and end

my_string = "i am a developer and python is a good PL"
substring = "a"

my_string.count(substring, 5 , 6)


# In[38]:


#find string through giving index number start and ending of index.
# returns nothing because 'is' ia at index 28, and we gave start point 1 and ednign point 20
my_string.find('is', 1, 20)


# In[41]:


#swap case, coverts all lower case to upper and vise versa.

my_string.swapcase()


# In[45]:


#replace a string 
# this will replace all 'a' to 'is'.
my_string.replace('a', 'is')


# In[47]:


#replace a string after setting count
# this will replace all 'a' to 'is' upto 2 count.
my_string.replace('a', 'is', 2)


# In[53]:


#sorting characters in order
sorted(my_string)


# In[54]:


#sorting characters in reverse order
sorted(my_string, reverse = True)


# In[ ]:




