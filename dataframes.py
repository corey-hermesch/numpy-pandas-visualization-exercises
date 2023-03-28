#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pydataset import data


# In[9]:


# Copy the code from the lesson to create a dataframe full of student grades.

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

df


# In[12]:


#     Create a column named passing_english that indicates whether each student has a passing grade in english.

df['passing_english'] = (df.english >= 70)
df


# In[21]:


#     Sort the english grades by the passing_english column. How are duplicates handled?

df.sort_values(by = 'passing_english')
# duplicates are orderd by the index


# In[186]:


#     Sort the english grades first by passing_english and then by student name. All the students that are 
# failing english should be first, and within the students that are failing english they should be ordered 
# alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to 
# the .sort_values method)

df.sort_values(by = 'name').sort_values(by = 'passing_english')

# let's see about the hint to use a list

df.sort_values(by = ['passing_english','name'])


# In[22]:


#     Sort the english grades first by passing_english, and then by the actual english grade, similar to how 
# we did in the last step.
df.sort_values(by = 'passing_english' and 'english')


# In[175]:


#     Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the 
# average of the math, english, and reading grades.

# following code did not change df, so I did it a different way
# df.assign(overall_grade = (df.math + df.english + df.reading) / 3) # didn't change df

df['overall_grade'] = (df.math + df.english + df.reading) / 3
df.head()


# In[174]:


# Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:

mpg = data('mpg')
mpg.head()
#data('mpg', show_doc=True)
mpg.head().info


# In[42]:


#     How many rows and columns are there?

mpg.shape


# In[58]:


#     What are the data types of each column?

mpg.dtypes


# In[172]:


#     Summarize the dataframe with .info and .describe

print(mpg.head().info)
mpg.describe()


# In[66]:


#     Rename the cty column to city.

mpg.columns
mpg = mpg.rename(columns = {'cty': 'city'})
mpg


# In[67]:


#     Rename the hwy column to highway.

mpg = mpg.rename(columns = {'hwy': 'highway'})
mpg


# In[171]:


#     Do any cars have better city mileage than highway mileage?

# No
mpg[mpg.city > mpg.highway].shape


# In[72]:


#     Create a column named mileage_difference this column should contain the difference between highway and 
# city mileage for each car.
mpg['mileage_difference'] = mpg.highway - mpg.city
mpg


# In[81]:


#     Which car (or cars) has the highest mileage difference?

# honda civic and vw new beetle both have a difference of 12
mpg.sort_values(by = 'mileage_difference', ascending = False).head()


# In[169]:


#     Which compact class car has the lowest highway mileage? The best?

print("The compact with the lowest highway mileage is the: ")
mpg[mpg['class'] == 'compact'].sort_values(by = 'highway', ascending=False).tail(1)


# In[96]:


print("The compact with the best highway mileage is the: ")
mpg[mpg['class'] == 'compact'].sort_values(by = 'highway', ascending=False).head(1)


# In[97]:


#     Create a column named average_mileage that is the mean of the city and highway mileage.

mpg['average_mileage'] = (mpg.city + mpg.highway) / 2
mpg


# In[101]:


#     Which dodge car has the best average mileage? The worst?
print("The Dodge with the best average mileage = ")
mpg[mpg['manufacturer'] == 'dodge'].sort_values('average_mileage', ascending = False).head(1)


# In[103]:


print("The Dodges with the worst average mileage = ")
mpg[mpg['manufacturer'] == 'dodge'].sort_values('average_mileage', ascending = False).tail(4)


# In[111]:


# Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:

mammals_df = data('Mammals')
mammals_df.head()
#data('Mammals', show_doc=True)


# In[112]:


#     How many rows and columns are there?

mammals_df.shape


# In[113]:


#     What are the data types?

mammals_df.dtypes


# In[168]:


#     Summarize the dataframe with .info and .describe
print(mammals_df.head().info)
mammals_df.describe()


# In[164]:


#     What is the the weight of the fastest animal?

# 3 different ways
mammals_df[mammals_df.speed == mammals_df.speed.max()]['weight'] # just the weight in a series with index #
mammals_df[mammals_df.speed == mammals_df.speed.max()]           # the whole row of max weight in df format
mammals_df.sort_values(by = 'speed', ascending=False).head(1)    # a row in df format


# In[160]:


#     What is the overal percentage of specials?


bool_mask = mammals_df.specials == True
mammals_df_special = mammals_df[bool_mask]
mammals_df_not_special = mammals_df[~bool_mask]

spcl_avg = mammals_df_special.shape[0] / mammals_df.shape[0]

print(f"There are {mammals_df_special.shape[0]} specials, and {mammals_df.shape[0]} total mammals.")
print("The overall percentage of 'specials' is: ")
print (round(spcl_avg * 100, 2))


# In[154]:


#     How many animals are hoppers that are above the median speed? What percentage is this?

num_hoppers = mammals_df[mammals_df['hoppers'] == True].shape[0]

num_hoppers_above_median_speed_df = mammals_df[(mammals_df['hoppers'] == True) & 
                                            (mammals_df.speed > mammals_df.speed.median())]

num_hoppers_above_median_speed = num_hoppers_above_median_speed_df.shape[0]

total_mammals = mammals_df.shape[0]

print("The number of hoppers with speeds above the median speed = ")
print(num_hoppers_above_median_speed)
print("The percentage of hoppers above the median speed out of all hoppers = ")
print(round((num_hoppers_above_median_speed / num_hoppers) * 100, 2))
print("The percentage of hoppers above the median speed out of all mammals = ")
print(round((num_hoppers_above_median_speed / total_mammals) * 100, 2))


# In[ ]:




