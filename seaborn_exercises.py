#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Use seaborn's load_dataset function to load the iris database to answer the following questions:


# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns


# In[2]:


iris_df = sns.load_dataset('iris')
iris_df.head()


# In[6]:


iris_df.info()


# In[7]:


#     What does the distribution of petal lengths look like?

sns.histplot(iris_df.petal_length)
plt.show()


# In[9]:


#     Is there a relationship between petal length and petal width?
# YES. Roughly, the greater the petal_length, the greater the petal_width
sns.scatterplot(data=iris_df, x=iris_df.petal_length, y = iris_df.petal_width)
plt.show()


# In[12]:


iris_df.head()


# In[23]:


#     Would it be reasonable to predict species based on sepal width and sepal length? For this, 
# you'll visualize two numeric columns through the lense of a categorical column.
#
# Disregard this few lines. see the relplot with hue further below
# plt.subplot(121)
# sns.stripplot(data=iris_df, x='species', y='sepal_length')

# plt.subplot(122)
# sns.stripplot(data=iris_df, x='species', y='sepal_width')
# plt.show()


# In[21]:


sns.relplot(data=iris_df, x='sepal_length', y='sepal_width', hue='species')
plt.show()
# You do have a grouping of setosa species, however versicolor and virginica have too much overlap


# In[24]:


#     Which features would be best used to predict species?

# petal_length vs petal_width would be more useful

sns.relplot(data=iris_df, x='petal_length', y='petal_width', hue='species')
plt.show()


# In[28]:


sns.pairplot(iris_df, hue='species', corner=True)
plt.show()


# In[29]:


#     Load the anscombe dataset from seaborn. Use pandas to group the data by the dataset column, and 
# calculate summary statistics for each dataset. What do you notice?

# we have four sets of x,y values that have similar summary statistics (but not the same)
ansc_df = sns.load_dataset('anscombe')


# In[34]:


ansc_df.head()
ansc_df.info()
I_df = ansc_df[ansc_df.dataset == 'I']
II_df = ansc_df[ansc_df.dataset == 'II']
III_df = ansc_df[ansc_df.dataset == 'III']
IV_df = ansc_df[ansc_df.dataset == 'IV']


# In[35]:


I_df.describe()


# In[36]:


II_df.describe()


# In[37]:


III_df.describe()


# In[38]:


IV_df.describe()


# In[53]:


ansc_df.columns


# In[65]:


#         Plot the x and y values from the anscombe data. Each dataset should be in a separate column.

# This doesn't seem exactly what is being asked, and it's marginally useful
sns.histplot(data=ansc_df)
plt.show()


# In[67]:


# This is much better:

sns.relplot(data=ansc_df, x='x', y='y',hue='dataset')
plt.show()


# In[69]:


#     Load the InsectSprays dataset from pydataset and read it's documentation. Create a boxplot that shows 
# the effectiveness of the different insect sprays.

from pydataset import data

ins_spray_df = data('InsectSprays')


# In[82]:


ins_spray_df.sample(5)


# In[81]:


#data('InsectSprays', show_doc=True)
ins_spray_df.head()


# In[83]:


sns.boxplot(data=ins_spray_df, x='spray',y='count')
plt.show()


# In[84]:


#     Load the swiss dataset from pydataset and read it's documentation. Create visualizations to answer the 
# following questions:
swiss_df = data('swiss')


# In[87]:


# data('swiss', show_doc=True)
swiss_df.head()


# In[90]:


#         Create an attribute named is_catholic that holds a boolean value of whether or not the province is 
# Catholic. (Choose a cutoff point for what constitutes catholic)

swiss_df['is_catholic'] = swiss_df.Catholic >= 40.0
swiss_df.is_catholic.value_counts()


# In[95]:


#         Does whether or not a province is Catholic influence fertility?

# Looks like yes, catholic provinces have higher fertility with some outliers

sns.boxplot(data=swiss_df, x='is_catholic', y='Fertility')
plt.show()


# In[100]:


#         What measure correlates most strongly with fertility?
# Could be Education (lower education = higher fertility)

sns.scatterplot(data=swiss_df, x='Education', y='Fertility')
plt.show()


# In[ ]:


#     Load the chipotle dataset from SQL, create a bar chart that shows the 4 most popular items and the 
# revenue produced by each.


# In[ ]:


#     Load the sleepstudy dataset from pydataset and read it's documentation. Use seaborn to create a line chart of all the individual subject's reaction times and a more prominant line showing the average change in reaction time.

