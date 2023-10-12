#!/usr/bin/env python
# coding: utf-8

# ![Capture.PNG](attachment:Capture.PNG)

# # Importing Required Libraries

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# # Importing Required Data Set

# In[2]:


df=pd.read_csv("UberDataset.csv")
print(df)


# # Understanding the Data Set

# In[3]:


df.head(10)


# In[4]:


df.tail(10)


# # Dataset stats

# In[5]:


df.shape


# In[6]:


df.columns


# In[7]:


df.info()


# In[8]:


df.describe()


# # Finding Null Values

# In[9]:


df.isnull()


# In[10]:


df.isnull().sum()


# In[ ]:


#There are null values


# # Removing Null Values

# In[11]:


df = df.dropna()


# In[12]:


df.isnull().any()


# In[13]:


df.isnull().sum()


# In[ ]:


#Now that there are no null values so we can start the analysis


# # Performing EDA

# In[26]:


average_value = df['MILES'].mean()

# Compare values with the average and categorize them
above_average = df[df['MILES'] > average_value].shape[0]
below_average = df[df['MILES'] <= average_value].shape[0]

# Data for the pie chart
sizes = [above_average, below_average]
labels = ['Above Average', 'Below Average']
colors = ['lightblue', 'lightcoral']

# Create a pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal') 

plt.title('Comparison of Values with Average')
plt.show()


# In[21]:


category_counts = df['CATEGORY'].value_counts()

# Create a pie chart
plt.figure(figsize=(4, 4))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Set1.colors)
plt.title('Distribution of Trips by Category', fontsize=16)
plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.

plt.show()


# In[15]:


plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='PURPOSE', palette='Set2')
plt.title('Count of Trips by Purpose', fontsize=16)
plt.xlabel('Purpose')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.show()


# In[16]:


plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='MILES', bins=20, kde=True, color='skyblue')
plt.title('Distribution of Trip Miles', fontsize=16)
plt.xlabel('Miles')
plt.ylabel('Frequency')
plt.show()


# In[18]:


mean_miles = df.groupby('CATEGORY')['MILES'].mean()
std_miles = df.groupby('CATEGORY')['MILES'].std()

# Create a bar plot with error bars
plt.figure(figsize=(10, 6))
sns.barplot(x=mean_miles.index, y=mean_miles.values, palette='viridis')
plt.errorbar(x=mean_miles.index, y=mean_miles.values, yerr=std_miles.values, fmt='none', c='black', capsize=5)
plt.title('Average Miles by Category', fontsize=16)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Average Miles', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# In[28]:


# least 5 start stations
least_5_start_stations = df['START'].value_counts().nsmallest(5)
least_5_start_stations


# In[39]:


least_5_start_stations = df['START'].value_counts().nsmallest(5)

# Create a pie chart
plt.figure(figsize=(4, 4))
plt.pie(least_5_start_stations, labels=least_5_start_stations.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Least 5 Start Stations (Pie Chart)', fontsize=16)
plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.

plt.show()


# In[29]:


# least 5 stop stations
least_5_stop_stations = df['STOP'].value_counts().nsmallest(5)
least_5_stop_stations


# In[34]:


least_5_stop_stations = df['STOP'].value_counts().nsmallest(5)

# Create a pie chart
plt.figure(figsize=(4, 4))
plt.pie(least_5_stop_stations, labels=least_5_stop_stations.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Least 5 Stop Stations', fontsize=16)
plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.

plt.show()


# In[30]:


top10_startstations


# In[31]:


top10_stopstations = df["START"].value_counts()[:10].sort_values(ascending=True)
top10_stopstations


# In[37]:


top10_startstations = df["START"].value_counts()[:10]

# Create a bar plot
plt.figure(figsize=(12, 6))
sns.barplot(x=top10_startstations.values, y=top10_startstations.index, palette='viridis')
plt.title('Top 10 Start Stations', fontsize=16)
plt.xlabel('Number of rides', fontsize=12)
plt.ylabel('Start Station', fontsize=12)
plt.show()

