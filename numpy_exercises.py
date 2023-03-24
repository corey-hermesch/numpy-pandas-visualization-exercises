#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[27]:


# Use the following code for questions below
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# In[12]:


# 1. How many negative numbers are there?
# Answer : 4
neg_a = a[a<0]
print(neg_a)
print(len(neg_a))


# In[13]:


# 2. How many positive numbers are there?
# Answer : 5

pos_a = a[a>0]
print(pos_a)
print(len(pos_a))


# In[14]:


#3. How many even positive numbers are there?
# Answer : 3

pos_even_a = a[(a > 0) & (a % 2 == 0)]
print(pos_even_a)
print(len(pos_even_a))


# In[17]:


#4. if you add 3 to each data point, how many positive numbers would there be?
# Answer : 3

print(len((a+3)[(a > 0) & (a % 2 == 0)]))


# In[19]:


#5. If you squared each number, what would the new mean and standard deviation be?

a_squared = a**2
print(f"a squared = {a_squared}")
print(f"a_squared mean = {a_squared.mean()}")
print(f"a_squared standard deviation = {a_squared.std()}")


# In[28]:


# 6. A common statistical operation on a dataset is centering. 
# This means to adjust the data such that the mean of the data is 0. 
# This is done by subtracting the mean from each data point. 
# Center the data set. 

print(a.mean())
a_centered = a - a.mean()
print(a_centered)
print(a_centered.mean())


# In[29]:


#7. Calculate the z-score for each data point. Recall z-score = (data point - mean) / std

a_zscore = (a - a.mean()) / a.std()
print(a_zscore)


# In[50]:


#8. More Numpy Practice
# setup

import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:


# In[54]:


# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

a_array = np.array(a)
sum_of_a = a_array.sum()
print(a_array)
print(sum_of_a)


# In[38]:


# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

min_of_a = a_array.min()
print(min_of_a)


# In[39]:


# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

max_of_a = a_array.max()
print(max_of_a)


# In[40]:


# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

mean_of_a = a_array.mean()
print(mean_of_a)


# In[43]:


# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the 
# numbers in the above list together

product_of_a = a_array.cumprod()[-1]
print(product_of_a)


# In[46]:


# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a 
# squared like [1, 4, 9, 16, 25...]

squares_of_a = np.arange(1,11) ** 2
print(squares_of_a)


# In[52]:


# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

odds_in_a = a_array[a_array % 2 == 1]
print (odds_in_a)


# In[55]:


# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

evens_in_a = a_array[a_array % 2 == 0]
print(evens_in_a)


# In[62]:


## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares
# for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]


# In[63]:


# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need 
# to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

print(f"for loop sum_of_b = {sum_of_b}")

b_array = np.array(b)
sum_of_b = b_array.sum()
print(f"array version = {sum_of_b}")


# In[66]:


# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

print(f"not numpy answer = {min_of_b}")

min_of_b = b_array.min()
print(f"numpy answer = {min_of_b}")


# In[67]:


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

print(f"not numpy answer = {max_of_b}")

max_of_b = b_array.max()
print(f"numpy answer = {max_of_b}")


# In[68]:


# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

print(f"not numpy answer = {mean_of_b}")

mean_of_b = b_array.mean()
print(f"numpy answer = {mean_of_b}")


# In[69]:


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

print(f"not numpy answer = {product_of_b}")

product_of_b = b_array.cumprod()[-1]
print(f"numpy answer = {product_of_b}")


# In[71]:


# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

print("not numpy answer = ")
print(squares_of_b)

squares_of_b = b_array ** 2
print("numpy answer = ")
print(squares_of_b)


# In[74]:


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

print(b_array)

print("not numpy answer = ")
print(odds_in_b)

odds_in_b = b_array[b_array % 2 == 1]
print("numpy answer = ")
print(odds_in_b)


# In[75]:


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

print(b_array)

print("not numpy answer = ")
print(evens_in_b)

evens_in_b = b_array[b_array % 2 == 0]
print("numpy answer = ")
print(evens_in_b)


# In[84]:


# Exercise 9 - print out the shape of the array b.

print(b_array)
print(np.shape(b_array))


# In[81]:


# Exercise 10 - transpose the array b.

print(b_array)
b_transpose = np.transpose(b_array)
print(b_transpose)


# In[88]:


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

print(b_array)
b_one_row = b_array.reshape(-1)
print(b_one_row)


# In[91]:


# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

b_array = np.ones((6, 1))
print(b_array)


# In[93]:


## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.

c_array = np.array(c)


# In[97]:


# Exercise 1 - Find the min, max, sum, and product of c.

print(f"min of c = {c_array.min()}")
print(f"max of c = {c_array.max()}")
print(f"sum of c = {c_array.sum()}")
print(f"product of c = {c_array.cumprod()[-1]}")


# In[99]:


# Exercise 2 - Determine the standard deviation of c.

print(f"std of c = {c_array.std()}")


# In[103]:


# Exercise 3 - Determine the variance of c.

print(f"var of c = {c_array.var()}")


# In[105]:


# Exercise 4 - Print out the shape of the array c

print(f"shape of c = {np.shape(c_array)}")


# In[106]:


# Exercise 5 - Transpose c and print out transposed result.

c_transpose = c_array.transpose()
print("c transposed = ")
print (c_transpose)


# In[107]:


# Exercise 6 - Get the dot product of the array c with c. 

print(np.dot(c_array, c_array))


# In[115]:


# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

print(c_array)
print(c_transpose)

c_product = c_array * c_transpose
print(c_product)
print(f"sum of c_array * c_transposed = {np.cumsum(c_product)[-1]}")


# In[116]:


# Exercise 8 - Write the code necessary to determine the product of c times c transposed. 
# Answer should be 131681894400.

c_product = c_array * c_transpose
print(c_product)
print(f"sum of c_array * c_transposed = {np.cumprod(c_product)[-1]}")


# In[118]:


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

d_array = np.array(d)


# In[119]:


# Exercise 1 - Find the sine of all the numbers in d

print (d_array.cumsum()[-1])


# In[125]:


# Exercise 2 - Find the cosine of all the numbers in d

d_radian_array = np.radians(d_array)
d_cosin_array = np.cos(d_radian_array)
print("cosine of d_array = ")
print(d_cosin_array)


# In[ ]:


# Exercise 3 - Find the tangent of all the numbers in d

# Exercise 4 - Find all the negative numbers in d

# Exercise 5 - Find all the positive numbers in d

# Exercise 6 - Return an array of only the unique numbers in d.

# Exercise 7 - Determine how many unique numbers there are in d.

# Exercise 8 - Print out the shape of d.

# Exercise 9 - Transpose and then print out the shape of d.

# Exercise 10 - Reshape d into an array of 9 x 2

