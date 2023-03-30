#!/usr/bin/env python
# coding: utf-8

# In[28]:


# Make a new Jupyter notebook named big_o_notation.ipynb

#     Title your chart "Big O Notation"
#     Label your x axis "Elements"
#     Label your y axis "Operations"
#     Label your curves or make a legend for the curves
#     Use LaTex notation where possible

# Curves to graph

#     y=0n+1

# and label the curve "O(1)"
# y=log(n)
# and label the curve "O(log n)"
# y=n
# and label the curve "O(n)"
# y=n∗log(n)
# and label it "O(n log n)"
# y=n2
# and label it "O(n^2)"
# y=2n
# and label it "O(2^n)"
# y=n!
# and label it "O(n!)"
# y=nn
# and label it "O(n^n)"

import numpy as np
import matplotlib.pyplot as plt


# In[26]:


# x has negative and positive values
# not all functiions can handle negative values, however.
# So, x2, x4, and x7 are positive-only values for their respective functions

x = list(range(-10,11,1))


y1 = [0*n + 1 for n in x]
y1_curve_label = '$O(1)$'

x2 = list(range(1,11,1))
y2 = [np.log(n) for n in x2]
y2_curve_label = '$O(log n)$'

y3 = [n for n in x]
y3_curve_label = '$O(n)$'

x4 = list(range(1,11,1))
y4 = [n*np.log(n) for n in x4]
y4_curve_label = '$O(n log n)$'

y5 = [n**2 for n in x]
y5_curve_label = '$O(n^2)$'

y6 = [2**n for n in x]
y6_curve_label = '$O(2^n)$'

x7 = list(range(1,11,1))
y7 = [np.math.factorial(n) for n in x7]
y7_curve_label = '$O(n!)$'

y8 = [n**n for n in x]
y8_curve_label = '$O(n^n)$'


# In[39]:


# Plotting all of these functions on the same chart doesn't make sense
# due to the large y values for some (n^n for instance)
# So, I commented out the last two, but perhaps should have commented out more

plt.plot(x, y1, c='red',label=y1_curve_label)
plt.plot(x2, y2, c='orange',label=y2_curve_label)
plt.plot(x, y3, c='gold', label=y3_curve_label)
plt.plot(x4, y4, c='green',label=y4_curve_label)
plt.plot(x, y5, c='blue', label=y5_curve_label)
plt.plot(x, y6, c='indigo', label=y6_curve_label)
#plt.plot(x7, y7, c='violet', label=y7_curve_label)
#plt.plot(x, y8, c='black', label=y8_curve_label)

plt.legend()
plt.title('Big O Notation')
plt.xlabel('Elements')
plt.ylabel('Operations')
plt.show()


# In[40]:


# Bonus. Write initials in block letters

x = list(range(1,11,1))
y = [0 for n in x]


# In[46]:


plt.plot(x,y)
# printing C
plt.hlines(3,1,2)
plt.vlines(1,1,3)
plt.hlines(1,1,2)

#printing H
plt.vlines(3,1,3)
plt.hlines(2,3,4)
plt.vlines(4,1,3)

plt.ylim(0,8,1)
plt.show()


# In[52]:


# # Would have to import scipy from somewhere
# x7 = np.arange(1,11)
# from scipy.specials import factorial
# y7 = factorial(x7)


# In[ ]:




