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


# In[3]:


# 1. Determine number of elements in fruits

print("number of elements in fruits = ")
print(fruits.size)
print(fruits.count())


# In[4]:


# 2. Output only the index from fruits

print("fruit index = ")
print(list(fruits.index))


# In[5]:


#3. Output only the values from fruits

print("fruit values = ")
print(fruits.values)


# In[6]:


#4. Confirm data type of values in fruits

print("fruits datatype = ")
print(type(fruits))
print("fruits.values datatype = ")
print(type(fruits.values))
print("fruits.index datatype = ")
print(type(fruits.index))
print("first element of fruit datatype = ")
print(type(fruits.values[0]))


# In[7]:


#5. Output only the first five values from fruits. Output the last three values. 
# Output two random values from fruits.

print("first five values from fruits = ")
print(fruits.head(5))
print("last two values from fruits = ")
print(fruits.tail(2))
print("two random fruits = ")

print(fruits[round(np.random.rand() * 100 % 17, 0)])
print(fruits[round(np.random.rand() * 100 % 17, 0)])
# OR (easier)
print(fruits.sample(2))


# In[8]:


#6. Run the .describe() on fruits to see what info it returns when called on a Series with string values

fruits.describe()


# In[9]:


#7. run the code necessary to produce only the unique string values from fruits

print("The unique values in fruits = ")
print(fruits.unique())
# OR
print(set(fruits))
print(type(set(fruits)))


# In[10]:


#8. Determine how many times each unique string value occurs in fruits

print("The number of each unique value in fruits and their count = ")
print(fruits.value_counts())


# In[11]:


#9. Determine the string value that occurs most frequently in fruits

print("The fruit that occurs most often in fruits = ")
print(fruits.describe().top)
print(f"with {fruits.describe().freq} occurrences")
# OR
fruits.value_counts().nlargest(n=1,keep='all')


# In[12]:


#10. Determine the string value that occurs least frequently in fruits

# print(type(fruits.value_counts()))
# a = fruits.value_counts()
# print(a.min())

print("The fruits that occur least frequently in the fruits series = ")
print(fruits.value_counts()[fruits.value_counts() == fruits.value_counts().min()])
# OR
fruits.value_counts().nsmallest(n=1, keep='all')


# In[13]:


###### Exercises Part 2 #########
# Explore more attributes and methods while you continue to work with the fruits Series.


# In[14]:


#     Capitalize all the string values in fruits.

fruits
cap_fruits = fruits.str.capitalize()
print("capitalized fruits = ")
print(cap_fruits)


# In[15]:


#     Count the letter "a" in all the string values (use string vectorization).

print(fruits.str.count('a'))
a_sum = sum(fruits.str.count('a'))
print ("The number of 'a's in all of the values in fruits = ")
print (a_sum)


# In[16]:


#     Output the number of vowels in each and every string value.

# vowels = list('aeiou')

# for fruit in fruits:
#     count = 0
#     f_letter_list = list(fruit)
#     for letter in f_letter_list:
#         if letter in vowels:
#             count += 1
#     print(f"{fruit} vowel count = {count}")

# There must be an easier way. I'll look for it later

# Different way, maybe easier

def count_vowels(s):
    count = 0
    for letter in s:
        if letter in 'aeiou':
            count += 1
    return count
print("Here is a series with the vowel counts of each element:")
print(fruits.apply(count_vowels))

# A nicer display using a DataFrame
fruits_df = pd.DataFrame(fruits)
fruits_df = fruits_df.rename(columns={0:'fruit_names'})
fruits_df['vowel_counts'] = fruits_df['fruit_names'].apply(count_vowels)
print ("Here is a DataFrame with the voel counts of each element:")
print(fruits_df)


# In[17]:


#     Write the code to get the longest string value from fruits.

fruits.describe()
fruits.str.count('')
f = fruits.str.count('')[fruits.str.count('') == fruits.str.count('').max()]
i_value = list(f.index)[0]
print("The longest string value from fruits = ")
print(fruits[i_value])

# Easier way below

print("An easier way to get the fruit with the longest string value:")
print(fruits[fruits.apply(len) == fruits.apply(len).max()])

# if you do it like below, you will get the element from the fruits Series
# that has the index of the max length of any fruit (which isn't what we want).
# So, the max length of the all the fruits is 16 (fruits[5] which is 'honeycrisp apple')
# fruits[16] is 'papaya'
print("The answer below is wrong. See comments for explanation:")
print(fruits[fruits.apply(len).max()])


# In[18]:


#     Write the code to get the string values with 5 or more letters in the name.

def count_letters(s):
    return len(s)

fruits[fruits.apply(count_letters) > 5]
# OR (easier way)
fruits[fruits.apply(len) > 5]
# OR
fruits[fruits.str.len() > 5]


# In[19]:


#     Find the fruit(s) containing the letter "o" two or more times.

def count_o(s):
    return s.count('o')

print("The fruits that contain the letter 'o' two or more times = ")
print(fruits[fruits.apply(count_o) >= 2])

# easier way
print("An easier way using string vectorization and boolean mask: ")
fruits[fruits.str.count('o') >= 2]


# In[20]:


#     Write the code to get only the string values containing the substring "berry".
def berry_test(s):
    return "berry" in s

print("The elements of fruits that contain 'berry' = ")
print(list(fruits[fruits.apply(berry_test)]))
print("An easier way using string vectorization and boolean mask:")
print(fruits[fruits.str.count('berry') >= 1])


# In[21]:


#     Write the code to get only the string values containing the substring "apple".

def apple_test(s):
    return "apple" in s

print("The elements of fruits that contain 'apple' = ")
print(list(fruits[fruits.apply(apple_test)]))
print("Another way using string vectorization and boolean mask")
print(fruits[fruits.str.count('apple') >= 1])


# In[22]:


#     Which string value contains the most vowels?

def count_vowels(s):
    count = 0
    for letter in s:
        if letter in 'aeiou':
            count += 1
    return count

print("The fruit that contains the most vowels = ")
fruits[fruits.apply(count_vowels).max()]
# Above only prints the string, though
# The code below will return the series "5    honeycrisp apple"
fruits[fruits.apply(count_vowels) == fruits.apply(count_vowels).max()]


# In[23]:


####### Exercises Part 3 #########

# Use pandas to create a Series named letters from the following string. The easiest way to make this string 
# into a Pandas series is to use list to convert each individual letter into a single string on a basic Python list.

letters = list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy')
letters = pd.Series(letters)
letters


# In[50]:


#     Which letter occurs the most frequently in the letters Series?

print("The letter that occurs most frequently = ")
print(letters.describe().top)
print("and it occurs this many times")
print(letters.describe().freq)
# OR
print(letters.value_counts().head(1))
# OR
print(letters.value_counts().idxmax())


# In[52]:


#     Which letter occurs the Least frequently?

#print(letters.value_counts())
print("The letter that occurs the least frequently = ")
print(letters[letters.value_counts().min()])
print("and it occurs this many times")
print(letters.value_counts().min())
# OR
print(letters.value_counts().nsmallest(1))


# In[54]:


#     How many vowels are in the Series?

print("The number of vowels in the series = ")
# use count_vowels function defined above
print(sum(letters.apply(count_vowels)))
print(letters.apply(count_vowels).sum())


# In[55]:


#     How many consonants are in the Series?

def count_consonants(s):
    count = 0
    for letter in s:
        if letter not in 'aeiou':
            count += 1
    return count

print("The number of consonants in the series = ")
print(sum(letters.apply(count_consonants)))
# The following uses the bitwise operator for not: '~'
# It doesn't work because I wasn't returning True or False; I was returning a count
print((~letters.apply(count_vowels)).sum())


# In[28]:


#     Create a Series that has all of the same letters but uppercased.

cap_letters = letters.str.upper()
cap_letters


# In[56]:


#     Create a bar plot of the frequencies of the 6 most commonly occuring letters.
import matplotlib.pyplot as plt

print(letters.value_counts())
letters.value_counts().head(6).plot()
# OR
letters.value_counts().head(6).plot(kind='bar')


# In[65]:


# use pandas to create a Series named numbers from the following list

numbers = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])


# In[31]:


#     What is the data type of the numbers Series?

# numbers is a series with dtype object (strings)

print(numbers.describe())
print(type(numbers))


# In[32]:


#     How many elements are in the number Series?

print("The number of elemnts in the number Series = ")
print(numbers.size)


# In[69]:


# Perform the necessary manipulations by accessing Series attributes and methods to convert the numbers 
# Series to a numeric data type.

# test
numbers[0].replace('$','').replace(',','')

# better way than below
float_numbers = numbers.str.replace('$','',regex=True).str.replace(',','',regex=True)
float_numbers

# OR

# float_numbers = numbers.str.replace(['$,','']) # this isn't quite right

# code to answer question
# float_numbers = []
# for number in numbers:
#     float_numbers.append(float((number.replace('$','')).replace(',','')))
# float_numbers = pd.Series(float_numbers)


# print(float_numbers)


# In[34]:


#     Run the code to discover the maximum value from the Series.

print("The maximum value from the numbers series = ")
print(float_numbers.max())


# In[35]:


#     Run the code to discover the minimum value from the Series.

print("The minimum value from the numbers series = ")
print(float_numbers.min())


# In[36]:


#     What is the range of the values in the Series?

print("The range of the values in the numbers series = ")
print(float_numbers.sort_values().min())
print("to")
print(float_numbers.sort_values().max())


# In[37]:


#     Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.

bin_series = pd.cut(float_numbers, 4)
print(bin_series.value_counts())


# In[38]:


#     Plot the binned data in a meaningful way. Be sure to include a title and axis labels.

b_s_vc = bin_series.value_counts().sort_values(ascending = False) # or sort_index()


# In[39]:


b_s_vc.plot.bar(title = 'Number of elements in 4 equally ranged bins',
               ).set(xlabel='Values', ylabel = 'Frequency')

# use matplotlib stuff plt.title ... then plt.show
# that will get rid of the line at the top [Text(0.5), ...


# In[40]:


# Use pandas to create a Series named exam_scores from the following list:

exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])


# In[41]:


#     How many elements are in the exam_scores Series?

print("The number of elements in the exam_scores Series = ")
print(exam_scores.size)


# In[42]:


#     Run the code to discover the minimum, the maximum, the mean, and the median scores for the exam_scores Series.

print("See below for the min, max, mean, median of exam_scores:")
print(exam_scores.describe())
print(f"median   {exam_scores.median()}")


# In[71]:


#     Plot the Series in a meaningful way and make sure your chart has a title and axis labels.

bin_exams = pd.cut(exam_scores,[0,60,70,80,90,100])

# below doesn't work:
# bin_exams = pd.cut(exam_scores,[100, 90, 80, 70, 60, 0])

bin_exams.value_counts(sort=False).plot.bar(title="Exam Scores, F-A").set(xlabel="Exam Scores", ylabel="Frequency")


# In[44]:


#     Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades. 
# Add the necessary points to the highest grade to make it 100, and add the same number of points to every other 
# score in the Series as well.

curve_value = 100 - exam_scores.max()
curved_grades = exam_scores + curve_value


# In[45]:


#     Use a method to convert each of the numeric values in the curved_grades Series into a categorical value 
# of letter grades. For example, 86 should be a 'B' and 95 should be an 'A'. Save this as a Series named 
# letter_grades.

def get_letter_grade(score):
    if score >= 90: return 'A'
    if score >= 80: return 'B'
    if score >= 70: return 'C'
    if score >= 60: return 'D'
    return 'F'

letter_grades = curved_grades.apply(get_letter_grade)


# In[46]:


#     Plot your new categorical letter_grades Series in a meaninful way and include a title and axis labels.
letter_grades_counts = letter_grades.value_counts()
sort_index = letter_grades_counts.index.sort_values()
letter_grades_counts[sort_index].plot.bar(title = "Exam Score Grades, A-F").set(
                                          xlabel = "Exam Letter Grades", ylabel = "Frequency")


# In[ ]:




