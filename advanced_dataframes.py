#!/usr/bin/env python
# coding: utf-8

# In[1]:


# advanced_dataframes exercises


# In[1]:


import numpy as np
import pandas as pd


# In[2]:


from env import host, user, password


# In[4]:


url = f'mysql+pymysql://{user}:{password}@{host}/employees'


# In[5]:


pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url)


# In[6]:


sql = '''
SELECT
    emp_no,
    first_name,
    last_name
FROM employees
WHERE gender = 'F'
LIMIT 100
'''


# In[7]:


pd.read_sql(sql,url)


# In[8]:


query = '''
SELECT
    t.title as title,
    d.dept_name as dept_name
FROM titles t
JOIN dept_emp USING (emp_no)
JOIN departments d USING (dept_no)
LIMIT 100
'''

title_dept = pd.read_sql(query, url)
title_dept.head()


# In[3]:


def get_db_url(db_name, user=user, host=host, password=password):
    '''
    get_db_url accepts a database name, username, hostname, password 
    and returns a url connection string formatted to work with codeup's 
    sql database.
    Default values from env.py are provided for user, host, and password.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'


# In[10]:


connection_string = get_db_url(user, host, password, 'employees')


# In[11]:


pd.read_sql(query, connection_string)


# In[ ]:


# If I intentionally make an error in the connection string (in this case, 
# I misspelled the database name), I get this error when I run the sql query:
# OperationalError: (pymysql.err.OperationalError) (1044, "Access denied for 
# user 'pagel_2179'@'%' to database 'employes'")

connection_string = get_db_url(user, host, password, 'employes')
pd.read_sql(query, connection_string)


# In[ ]:


# If I intentionally make an error in the SQL query (in this case,
# I removed the comma after title in the SELECT statement), I get this error:
# ProgrammingError: (pymysql.err.ProgrammingError) (1064, "You have an error 
# in your SQL syntax; ...
# The error looks very similar to the error that mysql would give if I 
# ran it in MySQLWorkBench

connection_string = get_db_url(user, host, password, 'employees')
error_query = '''
SELECT
    t.title as title
    d.dept_name as dept_name
FROM titles t
JOIN dept_emp USING (emp_no)
JOIN departments d USING (dept_no)
LIMIT 100
'''
pd.read_sql(error_query, connection_string)


# In[86]:


# Read the employees and titles tables into two separate DataFrames.

employees_db_connect_string = get_db_url('employees')
employees_query = '''
    SELECT *
    FROM employees
'''
titles_query = '''
    SELECT *
    FROM titles
'''


# In[13]:


employees_df = pd.read_sql(employees_query, employees_db_connect_string)


# In[14]:


titles_df = pd.read_sql(titles_query, employees_db_connect_string)


# In[ ]:


employees_df


# In[ ]:


titles_df


# In[ ]:


# How many rows and columns do you have in each DataFrame? Is that what you expected?

# employees_df had 300024 rows x 6 columns
# titles_df had 443308 rows x 4 columns
employees_df.shape


# In[15]:


titles_df.shape


# In[ ]:


# Display the summary statistics for each DataFrame.

employees_df.info()
#employees_df.describe()
titles_df.info()


# In[ ]:


# How many unique titles are in the titles DataFrame?

print("The number of unique titles in the titles DataFrame = ")
titles_df['title'].nunique()


# In[ ]:


# What is the oldest date in the to_date column?

print("The oldest date in the to_date columns are: ")
print(titles_df['to_date'].min())


# In[16]:


# What is the most recent date in the to_date column?

print("The most recent date in the to_date columns are: ")
print(titles_df['to_date'].max())


# In[19]:


# The most recent date in the to_date column that is not 9999-01-01 ?

(titles_df['to_date'][titles_df['to_date'] != titles_df['to_date'].max()]).max()


# In[ ]:


###### Exercise Part 2 ########


# In[4]:


#     Copy the users and roles DataFrames from the examples above.

# Create the users DataFrame

users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users


# In[5]:


# Create the roles DataFrame

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles


# In[6]:


#     What is the result of using a right join on the DataFrames?

pd.merge(users, roles, how='right', left_on='role_id', right_on='id')


# In[7]:


#     What is the result of using an outer join on the DataFrames?

pd.merge(users, roles, how='outer', left_on='role_id', right_on='id', indicator=True)


# In[9]:


#     What happens if you drop the foreign keys from the DataFrames and try to merge them?

# It doesn't work very well
users_without_role_id = users.drop(columns=['role_id'])
pd.merge(users_without_role_id, roles, how='outer', on = 'id')


# In[10]:


#     Load the mpg dataset from PyDataset.

from pydataset import data 

mpg = data('mpg')
mpg


# In[44]:


#     Output and read the documentation for the mpg dataset.

data('mpg', show_doc=True)
print(mpg.head())


# In[45]:


#     How many rows and columns are in the dataset?

# this is also in the show_doc=True documentation
mpg.shape


# In[11]:


#     Check out your column names and perform any cleanup you may want on them.

mpg = mpg.rename(columns={'cty': 'city', 'hwy': 'highway', 'class': 'car_class'})
mpg


# In[14]:


#     Display the summary statistics for the dataset.

mpg.describe(include='all')


# In[12]:


#     How many different manufacturers are there?

# Two ways. First, use nunique to count the number of unique manufacturers
mpg.manufacturer.nunique()

# OR use groupby and the 'manufacturer' column and then take the lenth
len(mpg.groupby('manufacturer').manufacturer.count())


# In[13]:


#     How many different models are there?

# Same two ways
mpg.model.nunique()

len(mpg.groupby('model').model.count())


# In[82]:


mpg.head()


# In[15]:


#     Create a column named mileage_difference like you did in the DataFrames exercises; this column 
# should contain the difference between highway and city mileage for each car.

# could do this the same way we did before:
#  mpg['mileage_difference'] = mpg.highway - mpg.city

# However, here is a way using pd.concat:
mileage_diff_df = pd.DataFrame(mpg.highway - mpg.city, columns=['mileage_difference'])
mpg = pd.concat([mpg, mileage_diff_df], axis = 1)
mpg


# In[25]:


#     Create a column named average_mileage like you did in the DataFrames exercises; this is the mean 
# of the city and highway mileage.

average_mileage = pd.DataFrame(((mpg.highway + mpg.city) / 2), columns = ['average_mileage'])
mpg = pd.concat([mpg, average_mileage], axis = 1)
mpg


# In[23]:


#     Create a new column on the mpg dataset named is_automatic that holds boolean values denoting whether 
# the car has an automatic transmission.

# could do this:
# mpg['is_automatic'] = mpg.trans.str.contains('auto')
# mpg
# mpg = mpg.drop(columns = ['is_automatic'])
 
# OR

# is_auto_df = pd.DataFrame(np.where(mpg.trans.str.contains('auto'), True, False), columns = ['is_automatic'])
# is_auto_df
# mpg = pd.concat([mpg, is_auto_df], axis=1)

#### is_auto_df has an index that starts with 0 which messes this up ####

# This works:
mpg.trans.value_counts()
mpg.trans.str.contains('auto')
mpg['is_auto'] = mpg.trans.str.contains('auto')
mpg = mpg.rename(columns = {'is_auto': 'is_automatic'})
mpg


# In[26]:


#     Using the mpg dataset, find out which which manufacturer has the best miles per gallon on average?

mpg

# get all of the average mpg's gouped by manufacturer and sort the highest to lowest
mpg.groupby('manufacturer').average_mileage.mean().sort_values(ascending=False)

# OR to just get the max average mileage with the manufacturer:
# pd.DataFrame(mpg.groupby('manufacturer').average_mileage.mean().sort_values(ascending=False)).iloc[0:1,:]


# In[27]:


#     Do automatic or manual cars have better miles per gallon?

# manual cars have better mpg's on average
pd.DataFrame(mpg.groupby('is_automatic').average_mileage.mean())


# In[164]:


mpg.groupby('manufacturer').model.count()


# In[168]:


is_auto_mask = np.where(mpg.trans.str.contains('auto'), True, False)
mpg[is_auto_mask]


# In[ ]:


######## Exercises Part 3 ########


# In[4]:


#     Use your get_db_url function to help you explore the data from the chipotle database.

connection_string = get_db_url('chipotle')
query = """
    SELECT *
    FROM orders
"""


# In[140]:


orders = pd.read_sql(query, connection_string)


# In[141]:


orders_df = orders
orders_df.head()


# In[142]:


#     What is the total price for each order?

# def get_money_float(s):
#     s = s.strip('$ ')
#     return round(float(s),2)

# item_price_float = orders_df.item_price.apply(get_money_float)
# orders_df = orders_df.drop(columns = ['item_price'])
# orders_df.head()

# OR 
orders_df.item_price = orders_df.item_price.str.strip('$').astype(float)
# that would have been so much easier


# In[144]:


orders_df
orders_df.info()


# In[145]:


order_total_price = pd.DataFrame(orders_df.groupby('order_id').item_price.sum())
order_total_price.head()


# In[139]:


#     What are the most popular 3 items?

orders_df.head()
orders_df.groupby('item_name').quantity.sum().sort_values(ascending=False).head(3)


# In[147]:


#     Which item has produced the most revenue?

# turns out item_price was not price per, for example, chicken bowl; item_price was the price
# for 1 item which may have included 2 chicken bowls

orders_df.groupby(['item_name']).item_price.sum().sort_values(ascending=False).head(1)


# In[84]:


#     Join the employees and titles DataFrames together.

employees_db_connect_string = get_db_url('employees')
employees_query = '''
    SELECT *
    FROM employees
'''
titles_query = '''
    SELECT *
    FROM titles
'''


# In[85]:


employees_df = pd.read_sql(employees_query, employees_db_connect_string)


# In[87]:


titles_df = pd.read_sql(titles_query, employees_db_connect_string)


# In[88]:


employees_df.head()


# In[89]:


titles_df.head()


# In[136]:


emp_titles_df = pd.merge(employees_df, titles_df, how='inner', on='emp_no')
emp_titles_df.head()


# In[138]:


#     For each title, find the hire date of the employee that was hired most recently with that title.

hire_date_max_df = pd.DataFrame(emp_titles_df.groupby(['title']).hire_date.max())
hire_date_max_df

# Now, how do I get their names? Will come back


# In[127]:


emp_titles_df[['title','hire_date']] == hire_date_max_df
#mask = np.where()
#emp_titles_df[['title','first_name','last_name','hire_date']].groupby(['title']).hire_date.max()


# In[95]:


#     Write the code necessary to create a cross tabulation of the number of titles by department. 
# (Hint: this will involve a combination of SQL code to pull the necessary data and python/pandas code 
# to perform the manipulations.)

title_dept_query = '''
SELECT DISTINCT(title), dept_name
FROM titles
	JOIN dept_emp USING(emp_no)
    JOIN departments USING(dept_no)
'''

title_dept_df = pd.read_sql(title_dept_query, employees_db_connect_string)


# In[96]:


title_dept_df.head()


# In[98]:


pd.crosstab(title_dept_df.dept_name, title_dept_df.title, margins = True)


# In[99]:


#Another way
title_dept_df.groupby('dept_name').title.nunique()


# In[ ]:




