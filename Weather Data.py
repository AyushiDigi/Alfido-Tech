#!/usr/bin/env python
# coding: utf-8

# ![W.png](attachment:W.png)

# # Importing Required Libraries

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# # Importing Required Data Set

# In[2]:


df=pd.read_csv("Weather Data.csv")
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


#Now that there are no null values so we can start the analysis


# # Performing EDA

# In[13]:


weather= df['Weather'].unique()
for weathers in weather:
    print("->",weathers)


# In[30]:


df[df.Weather == 'Clear']


# In[11]:


plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Temp_C', bins=20, kde=True)
plt.title('Distribution of Temperature (Celsius)')
plt.xlabel('Temperature (Celsius)')
plt.ylabel('Frequency')
plt.show()


# In[15]:


wind_speed = df['Wind Speed_km/h'].nunique()
print('Wind Speed km/h:-',wind_speed)


# In[12]:


numerical_columns = ['Temp_C', 'Dew Point Temp_C', 'Rel Hum_%', 'Wind Speed_km/h', 'Visibility_km', 'Press_kPa']
df[numerical_columns].hist(bins=15, figsize=(15, 10))
plt.suptitle('Histograms of Numerical Columns', fontsize=16)
plt.show()


# In[16]:


plt.figure(figsize=(15, 8))
sns.boxplot(data=df[numerical_columns])
plt.title('Box Plots of Numerical Columns', fontsize=16)
plt.xticks(rotation=45)
plt.show()


# In[17]:


from wordcloud import WordCloud
plt.figure(figsize=(10, 10))
wordcloud = WordCloud(width=800, height=800, background_color='white').generate(' '.join(df['Weather']))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('Word Cloud of Weather Conditions', fontsize=16)
plt.axis('off')
plt.show()


# In[20]:


plt.figure(figsize=(15, 8))
for column in monthly_data.columns:
    sns.lineplot(data=monthly_data, x=monthly_data.index, y=column, label=column)
plt.title('Monthly Averages of Numerical Columns', fontsize=16)
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()


# In[21]:


pairplot = sns.pairplot(df[numerical_columns], diag_kind='kde')
pairplot.fig.suptitle('Pairplot of Numerical Columns', y=1.02, fontsize=16)

# Adjust plot layout to prevent overlap
plt.tight_layout()
plt.show()


# In[22]:


plt.figure(figsize=(10, 6))
correlation_matrix = df[numerical_columns].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap', fontsize=16)
plt.show()


# In[23]:


plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x=df.index, y='Temp_C', label='Temperature (°C)')
sns.lineplot(data=df, x=df.index, y='Rel Hum_%', label='Relative Humidity (%)')
plt.title('Time Series of Temperature and Relative Humidity', fontsize=16)
plt.xlabel('Date/Time')
plt.ylabel('Value')
plt.legend()
plt.show()


# In[28]:


plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Wind Speed_km/h', y='Visibility_km', alpha=0.5)
plt.title('Wind Speed vs. Visibility')
plt.xlabel('Wind Speed (km/h)')
plt.ylabel('Visibility (km)')
plt.tight_layout()
plt.show()

