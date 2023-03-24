#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Pandas Exercises Part I
import pandas as pd
import numpy as np

# from pydataset import data


# In[2]:


fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple"
                    , "gala apple", "honeycrisp apple", "tomato"
                    , "watermelon", "honeydew", "kiwi", "kiwi"
                    , "kiwi", "mango", "blueberry", "blackberry"
                    , "gooseberry", "papaya"])


# In[55]:


# 1. Determine number of elements in fruits

print("number of elements in fruits = ")
print(fruits.size)
print(fruits.count())


# In[37]:


# 2. Output only the index from fruits

print("fruit index = ")
print(list(fruits.index))


# In[9]:


#3. Output only the values from fruits

print("fruit values = ")
print(fruits.values)


# In[17]:


#4. Confirm data type of values in fruits

print("fruits datatype = ")
print(type(fruits))
print("fruits.values datatype = ")
print(type(fruits.values))
print("first element of fruit datatype = ")
print(type(fruits.values[0]))


# In[40]:


#5. Output only the first five values from fruits. Output the last three values. 
# Output two random values from fruits.

print("first five values from fruits = ")
print(fruits.head(5))
print("last two values from fruits = ")
print(fruits.tail(2))
print("two random fruits = ")

print(fruits[round(np.random.rand() * 100 % 17, 0)])
print(fruits[round(np.random.rand() * 100 % 17, 0)])


# In[41]:


#6. Run the .describe() on fruits to see what info it returns when called on a Series with string values

fruits.describe()


# In[48]:


#7. run the code necessary to produce only the unique string values from fruits

print("The unique values in fruits = ")
print(fruits.unique())


# In[49]:


#8. Determine how many times each unique string value occurs in fruits

print("The number of each unique value in fruits and their count = ")
print(fruits.value_counts())


# In[58]:


#9. Determine the string value that occurs most frequently in fruits

print("The fruit that occurs most often in fruits = ")
print(fruits.describe().top)
print(f"with {fruits.describe().freq} occurrences")


# In[79]:


#10. Determine the string value that occurs least frequently in fruits

# print(type(fruits.value_counts()))
# a = fruits.value_counts()
# print(a.min())

print("The fruits that occur least frequently in the fruits series = ")
print(fruits.value_counts()[fruits.value_counts() == fruits.value_counts().min()])


# In[ ]:




