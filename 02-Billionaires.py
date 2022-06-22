#!/usr/bin/env python
# coding: utf-8

# # Homework 5, Part 2: Answer questions with pandas
# 
# **Use the Excel file to answer the following questions.** This is a little more typical of what your data exploration will look like with pandas.

# ## 0) Setup
# 
# Import pandas **with the correct name** .

# In[1]:


import pandas as pd


# ## 1) Reading in an Excel file
# 
# Use pandas to read in the `richpeople.xlsx` Excel file, saving it as a variable with the name we'll always use for a dataframe.
# 
# > **TIP:** You will use `read_excel` instead of `read_csv`. Trying `read_excel` the first time will probably not work, you'll get an error message. Be sure to read the error carefully: *you probably need to install a new library before it will work, and the error tells you what the library is named*.

# In[2]:


df = pd.read_excel("richpeople.xlsx")


# ## 2) Checking your data
# 
# Display the number of rows and columns in your data. Also display the names and data types of each column.

# In[3]:


df.shape


# In[4]:


df.dtypes


# ## 3) Who are the top 10 richest billionaires? Use the `networthusbillion` column.

# In[5]:


df.sort_values(by="networthusbillion", ascending=False).head(10)


# ## 4) How many male billionaires are there compared to the number of female billionares? What percent is that? Do they have a different average wealth?
# 
# > **TIP:** The last part uses `groupby`, but the count/percent part does not.
# > **TIP:** When I say "average," you can pick what kind of average you use.

# In[6]:


df.gender.value_counts()


# In[7]:


male = df[df.gender == "male"]
female = df[df.gender == "female"]

pct_male = (male.shape[0] / df.gender.value_counts().sum()) * 100
pct_female = (female.shape[0] / df.gender.value_counts().sum()) * 100

print(f"{pct_male:.2f}%")
print(f"{pct_female:.2f}%")


# In[8]:


df.groupby(by="gender").networthusbillion.mean()


# ## 5) What is the most common source/type of wealth? Is it different between males and females?
# 
# > **TIP:** You know how to `groupby` and you know how to count how many times a value is in a column. Can you put them together???
# > **TIP:** Use percentages for this, it makes it a lot more readable.

# In[9]:


df.typeofwealth.value_counts()


# In[10]:


df.typeofwealth.mode()


# ## 6) What companies have the most billionaires? Graph the top 5 as a horizontal bar graph.
# 
# > **TIP:** First find the answer to the question, then just try to throw `.plot()` on the end
# >
# > **TIP:** You can use `.head()` on *anything*, not just your basic `df`
# >
# > **TIP:** You might feel like you should use `groupby`, but don't! There's an easier way to count.
# >
# > **TIP:** Make the largest bar be at the top of the graph
# >
# > **TIP:** If your chart seems... weird, think about where in the process you're sorting vs using `head`

# In[11]:


import matplotlib


# In[12]:


df.sourceofwealth.value_counts().head(5).sort_values(ascending=True).plot.barh()


# ## 7) How much money do these billionaires have in total?

# In[13]:


money_total = df.networthusbillion.sum()
money_total


# ## 8) What are the top 10 countries with the most money held by billionaires?
# 
# I am **not** asking which country has the most billionaires - this is **total amount of money per country.**
# 
# > **TIP:** Think about it in steps - "I want them organized by country," "I want their net worth," "I want to add it all up," and "I want 10 of them." Just chain it all together.

# In[14]:


df.groupby(by="countrycode").networthusbillion.sum().head(10).sort_values(ascending=False)


# ## 9) How old is an average billionaire? How old are self-made billionaires  vs. non self-made billionaires? 

# In[15]:


avg_age_billionaire = df.age.mean()

print(f"The average age of a billionarie is {avg_age_billionaire}.")


# In[16]:


self_made = df[df.selfmade == "self-made"].age.mean()
non_self_made = df[df.selfmade != "self-made"].age.mean()

print(f"The average age of a self-made billionarie is {self_made}.")
print(f"The average age of a non self-made billionarie is {non_self_made}.")


# ## 10) Who are the youngest billionaires? Who are the oldest? Make a graph of the distribution of ages.
# 
# > **TIP:** You use `.plot()` to graph values in a column independently, but `.hist()` to draw a [histogram](https://www.mathsisfun.com/data/histograms.html) of the distribution of their values

# In[17]:


youngest_b = df.age.min()
print(f"The youngest billionaire is {youngest_b:.0f} years old.")


# In[18]:


oldest_b = df.age.max()
print(f"The oldest billionaire is {oldest_b:.0f} years old.")


# In[19]:


# df.age.plot()
df.age.hist()


# ## 11) Make a scatterplot of net worth compared to age

# In[20]:


df.plot.scatter(x="networthusbillion", y="age")


# ## 13) Make a bar graph of the wealth of the top 10 richest billionaires
# 
# > **TIP:** When you make your plot, you'll need to set the `x` and `y` or else your chart will look _crazy_
# >
# > **TIP:** x and y might be the opposite of what you expect them to be

# In[21]:


df.sort_values(by="networthusbillion", ascending=False).head(10).plot(kind="bar", x="name", y="networthusbillion")

