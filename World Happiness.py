#!/usr/bin/env python
# coding: utf-8

# ![W%20%281%29.png](attachment:W%20%281%29.png)

# # Importing Required Libraries

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# # Importing Required Data Set

# In[3]:


df=pd.read_csv("world_happiness_2016.csv")
print(df)


# # Understanding the Data Set

# In[4]:


df.head(10)


# In[5]:


df.tail(10)


# # Dataset stats

# In[6]:


df.shape


# In[7]:


df.columns


# In[8]:


df.info()


# In[9]:


df.describe()


# # Finding Null Values

# In[10]:


df.isnull()


# In[11]:


df.isnull().sum()


# In[ ]:


#Now that there are no null values so we can start the analysis


# # Performing EDA

# In[35]:


dumm = df.loc[:, "Happiness Score": ]
plt.figure(figsize = (11, 5))
plt.xticks(fontsize=7,rotation=45)
sns.boxplot(dumm)


# In[12]:


plt.figure(figsize=(10, 6))
sns.histplot(df['Happiness Score'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Happiness Score', fontsize=16)
plt.xlabel('Happiness Score')
plt.ylabel('Frequency')
plt.show()


# In[14]:


plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Region', y='Happiness Score', palette='viridis')
plt.title('Happiness Score by Region', fontsize=16)
plt.xlabel('Region', fontsize=12)
plt.ylabel('Happiness Score', fontsize=12)
plt.xticks(rotation=90)
plt.show()


# In[17]:


numerical_columns = ['Happiness Rank', 'Happiness Score', 'Lower Confidence Interval', 
                     'Upper Confidence Interval', 'Economy (GDP per Capita)', 'Family',
                     'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)',
                     'Generosity', 'Dystopia Residual']

# Calculate the correlation matrix
correlation_matrix = df[numerical_columns].corr()

# Create a correlation heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap for Numerical Columns', fontsize=16)
plt.show()


# In[21]:


numerical_columns = ['Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)', 'Freedom',
                     'Trust (Government Corruption)', 'Generosity']

# Create the pairplot
pairplot = sns.pairplot(df[numerical_columns], diag_kind='kde', height=2)

# Adjust the position of the subtitle
pairplot.fig.suptitle('Pairplot of Key Numerical Columns', y=1.02, fontsize=16)

plt.show()


# In[19]:


plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='Region', y='Trust (Government Corruption)', palette='viridis')
plt.title('Trust in Government Corruption by Region', fontsize=16)
plt.xlabel('Region', fontsize=12)
plt.ylabel('Trust (Government Corruption)', fontsize=12)
plt.xticks(rotation=90)
plt.show()


# In[22]:


plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Dystopia Residual', bins=20, kde=True, color='skyblue')
plt.title('Distribution of Dystopia Residual', fontsize=16)
plt.xlabel('Dystopia Residual', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.show()


# In[24]:


plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Happiness Score', y='Trust (Government Corruption)', palette='viridis')
plt.title('Trust in Government Corruption vs. Happiness Score', fontsize=16)
plt.xlabel('Happiness Score', fontsize=12)
plt.ylabel('Trust (Government Corruption)', fontsize=12)
plt.grid(True)
plt.show()


# In[26]:


trust_categories = ['Low', 'Medium', 'High']
df['Trust Category'] = pd.cut(df['Trust (Government Corruption)'], bins=[0, 0.3, 0.6, 1.0], labels=trust_categories)

# Calculate the count of each trust category
trust_category_counts = df['Trust Category'].value_counts()

# Create a pie chart
plt.figure(figsize=(4, 4))
plt.pie(trust_category_counts, labels=trust_category_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Set1.colors)
plt.title('Distribution of Trust Categories', fontsize=16)
plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.

plt.show()


# In[ ]:




