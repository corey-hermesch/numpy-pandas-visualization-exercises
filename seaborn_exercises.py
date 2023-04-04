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


# In[78]:


#     Load the anscombe dataset from seaborn. Use pandas to group the data by the dataset column, and 
# calculate summary statistics for each dataset. What do you notice?

# we have four sets of x,y values that have similar summary statistics (but not the same)
ansc_df = sns.load_dataset('anscombe')


# In[82]:


ansc_df.head()
ansc_df.info()

I_df = ansc_df[ansc_df.dataset == 'I']
II_df = ansc_df[ansc_df.dataset == 'II']
III_df = ansc_df[ansc_df.dataset == 'III']
IV_df = ansc_df[ansc_df.dataset == 'IV']


# In[83]:


I_df.describe()


# In[36]:


II_df.describe()


# In[37]:


III_df.describe()


# In[38]:


IV_df.describe()


# In[84]:


ansc_df.columns


# In[85]:


#         Plot the x and y values from the anscombe data. Each dataset should be in a separate column.

# This doesn't seem exactly what is being asked, and it's marginally useful
sns.histplot(data=ansc_df)
plt.show()


# In[88]:


# This is much better:

sns.relplot(data=ansc_df, x='x', y='y',col='dataset')
plt.show()


# In[4]:


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


# In[5]:


#     Load the swiss dataset from pydataset and read it's documentation. Create visualizations to answer the 
# following questions:
swiss_df = data('swiss')


# In[87]:


# data('swiss', show_doc=True)
swiss_df.head()


# In[6]:


#         Create an attribute named is_catholic that holds a boolean value of whether or not the province is 
# Catholic. (Choose a cutoff point for what constitutes catholic)

swiss_df['is_catholic'] = swiss_df.Catholic >= 50.0
swiss_df.is_catholic.value_counts()


# In[7]:


#         Does whether or not a province is Catholic influence fertility?

# Looks like yes, catholic provinces have higher fertility with some outliers

sns.boxplot(data=swiss_df, x='is_catholic', y='Fertility')
plt.show()


# In[91]:


#         What measure correlates most strongly with fertility?
# Could be Education (lower education = higher fertility)

sns.scatterplot(data=swiss_df, x='Education', y='Fertility')
plt.show()


# In[90]:


# correlation function correlates every variable with every other variable
# then using heatmap helps see the correlations (and the negative correlations)
# cmap = 'Blues' is more readable than the default
sns.heatmap(swiss_df.corr(), annot=True, cmap='Blues')
plt.show()


# In[75]:


#     Load the chipotle dataset from SQL, create a bar chart that shows the 4 most popular items and the 
# revenue produced by each.

# in retrospect, I answered the wrong question. I charted the top earning items

from env import host, user, password

def get_db_url(db_name, user=user, host=host, password=password):
    '''
    get_db_url accepts a database name, username, hostname, password 
    and returns a url connection string formatted to work with codeup's 
    sql database.
    Default values from env.py are provided for user, host, and password.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'
    
connection = get_db_url('chipotle')
query = "SELECT * FROM orders"
chip_df = pd.read_sql(query, connection)
chip_df.head()


# In[95]:


#change item_price to float
chip_df.item_price = chip_df.item_price.str.strip('$').astype(float)
chip_df.info()


# In[ ]:


# group item_names together with the sum of their item_price (item_price includes quantity, i.e. you don't
# have to multipy item_price x quantity to get a total; item_price IS a total)

revenue_by_item = chip_df.groupby(by='item_name').item_price.sum().sort_values(ascending=False)


# In[104]:


# change series from above to a DF
revenue_df = pd.DataFrame(revenue_by_item)
revenue_df = revenue_df.reset_index()
# plot the desired info
sns.catplot(data=revenue_df.head(4), x = 'item_name', y = 'item_price', kind='bar')
plt.xlabel('Item Name')
# plt.ylabel('Total Revenue')
plt.title('Top 4 Grossing Chipotle Menu Items')
plt.show()


# In[63]:


#     Load the sleepstudy dataset from pydataset and read it's documentation. Use seaborn to create a line chart 
# of all the individual subject's reaction times and a more prominant line showing the average change in reaction 
# time.

sleep_df = data('sleepstudy')
# data('sleepstudy', show_doc=True)
# data.head()
sleep_df.head(12)


# In[74]:


# All of the subjects reaction times (a mess)
sns.lineplot(data=sleep_df, x='Days', y = 'Reaction', hue='Subject', palette='bright')
plt.legend('')
plt.show()


# In[69]:


# Average reaction time only
avg_rxn_time = sleep_df.groupby(by='Days').Reaction.mean()
avg_rxn_time_df = pd.DataFrame(avg_rxn_time)
sns.lineplot(data=avg_rxn_time_df, x='Days', y='Reaction')
plt.show()


# In[71]:


# This one looks the best / most useful
# could also run sns.relplot twice and have the graphs on top of each other
sns.relplot(data=sleep_df, x='Days', y='Reaction', kind='line')
plt.show()


# In[ ]:




