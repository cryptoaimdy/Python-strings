#!/usr/bin/env python
# coding: utf-8

# In[35]:


# string indexing and slicing
s = "crypto aimdy"
# printing a character in string using positive index number
print(s[5])
# printing a character in string using negative index number
print(s[-5])


# In[28]:


##String Slicing

#printing string upto 5 characters
print(s[:5])


# In[29]:


#prints string after first leaving first 5 char
print(s[5:])


# In[30]:


#prints char at position 4 all the way upto char at position 5 but leaving the character 5.
print(s[4:5])


# In[31]:


#prints all the char from opposite side after leaving first eight char from backwards.
print(s[:-8])


# In[32]:


#pritns cahr from backward at index 2.
print(s[-2])


# In[33]:


#prints the every character at the gap of 5 characters after priting each character.
print(s[::5])


# In[34]:


#prints the every character from backwards at the gap of 3 characters after priting each character.
print(s[::-3])


# In[37]:


# string length
#printing string length
print(len(s))


# In[43]:


#Instead of using a variable, we can also pass a string right into the len() method:
print(len("Let's print the length of this string."))


# In[ ]:




