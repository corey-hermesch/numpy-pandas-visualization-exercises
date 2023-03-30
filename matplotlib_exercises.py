#!/usr/bin/env python
# coding: utf-8

# In[61]:


# Use matplotlib to plot the following equation:
# y=x^2−x+2

# You'll need to write the code that generates the x and y points.

# Add an anotation for the point 0, 0, the origin.

x = list(range(-50,51,1))
y = [n**2 for n in x]


# In[62]:


import matplotlib.pyplot as plt


# In[63]:


plt.plot(x,y)
plt.annotate('origin',xy=(0,0),xytext=(0,400),arrowprops={'arrowstyle': 'simple'})
plt.show()


# In[68]:


# Create and label 4 separate charts for the following equations (choose a range for x that makes sense):

# y1 - y=√x
# y2 - y=x^3
# y3 - y=2^x
# y4 - y=1/(x+1)

# You can use functions from the math module to help implement some of the equations above.

x = list(range(-50,50,2))
x1 = list(range(0,50,2)) # took out negatives for the y1 since it is asking for square roots
x3 = list(range(-10,10,1)) # made x3 smaller range since 2^n gets so large

y1 = [n**.5 for n in x1]
y2 = [n**3 for n in x]
y3 = [2**n for n in x3]
y4 = [1/(n+1) for n in x]

# could have used arrays and it's a little quicker:
# x = array(range(-50,51,2))
# y = x**.5


# In[65]:


# y1 chart
plt.plot(x1,y1)
plt.title('$y = √x$')
plt.xlabel('$x$')
plt.ylabel('$y$',rotation=0)
plt.xlim(-50,50)
plt.show()


# In[31]:


#y2 chart
plt.plot(x,y2)
plt.title('$y = x^3$')
plt.xlabel('$x$')
plt.ylabel('$y$',rotation=0)

plt.show()


# In[38]:


# y3 chart
plt.plot(x3,y3)
plt.title('$y = 2^x$')
plt.xlabel('$x$')
plt.ylabel('$y$',rotation=0)
plt.xlim(-10,10)
plt.show()


# In[60]:


# y 4 chart
plt.plot(x,y4)
plt.title('$y = 1/(x+1)$\n(Note: x = -1 results in dividing by zero)')
plt.xlabel('$x$')
plt.ylabel('$y$',rotation=0)
plt.xlim(-50,50)
plt.show()


# In[72]:


# put all four charts from above into one large figure with 4 subplots

## this is spitting out 4 rows of charts with 1 column, and I'm not sure why
## Will try to fix later

# y1 chart

plt.subplot(2,2,1)
plt.plot(x1,y1)
plt.title('$y = √x$')
plt.xlabel('$x$')
plt.ylabel('$y$',rotation=0)
plt.xlim(-50,50)
plt.show()

#y2 chart
plt.subplot(2,2,2)
plt.plot(x,y2)
plt.title('$y = x^3$')
plt.xlabel('$x$')
plt.ylabel('$y$',rotation=0)
plt.xlim(-50,50)
plt.show()

# y3 chart
plt.subplot(2,2,3)
plt.plot(x3,y3)
plt.title('$y = 2^x$')
plt.xlabel('$x$')
plt.ylabel('$y$',rotation=0)
plt.xlim(-10,10)
plt.show()

# y4 chart
plt.subplot(2,2,4)
plt.plot(x,y4)
plt.title('$y = 1/(x+1)$\n(Note: x = -1 results in dividing by zero)')
plt.xlabel('$x$')
plt.ylabel('$y$',rotation=0)
plt.xlim(-50,50)

plt.show()


# In[56]:


# Combine the figures you created in the last step into one figure where each of the 4 equations has a 
# different color for the points. Be sure to include a legend and an appropriate title for the figure.

# y1 chart
plt.plot(x1,y1,c='red',label='$y = √x$')

#y2 chart
plt.plot(x,y2,c='blue', label='$y = x^3$')

# y3 chart
plt.plot(x3,y3,c='indigo', label='$y = 2^x$')

# y4 chart
plt.plot(x,y4,c='green', label='$y = 1/(x+1)$')

# For all charts
plt.xlabel('$x$')
plt.ylabel('$y$',rotation=0)
plt.xlim(-10,10)
plt.ylim(-50,50)
plt.title('Various plots')
plt.legend()

plt.show()


# In[ ]:




