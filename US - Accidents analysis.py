#!/usr/bin/env python
# coding: utf-8

# # Importing the Libraries

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# # Loading the Data

# In[2]:


df=pd.read_csv("D:\\US_Accidents_March23.csv")
df.head()


# # Data Preprocessing

# In[ ]:


df.info()


# In[ ]:


df.columns


# In[ ]:


len(df.columns)


# In[ ]:


df.describe()


# In[ ]:


numeric=["int16","int32","int64","float16","float32","float64"]
numeric_df=df.select_dtypes(include=numeric)
len(numeric_df.columns)


# In[ ]:


df.isnull().sum().sort_values(ascending=False)


# In[ ]:


missing_percentage=df.isnull().sum().sort_values(ascending=False)/len(df)
missing_percentage


# In[ ]:


type(missing_percentage)


# In[ ]:


missing_percentage[missing_percentage !=0]


# In[ ]:


missing_percentage[missing_percentage !=0].plot(kind="barh")


# # columns for analysis( city, start time)

# In[ ]:


cities=df.City.unique()
cities


# In[ ]:


len(cities)


# In[ ]:


cities_by_accident=df.City.value_counts()
cities_by_accident


# In[ ]:


cities_by_accident[:10]


# In[ ]:


"newyork" in df.City


# In[ ]:


"NY" in df.State


# In[ ]:


cities_by_accident[:20].plot(kind="barh")


# In[ ]:


sns.distplot(cities_by_accident)
plt.show()


# In[ ]:


high_accident_cities=cities_by_accident[cities_by_accident>=1000]
low_accident_cities=cities_by_accident[cities_by_accident<1000]


# In[ ]:


len(high_accident_cities)/len(cities)


# In[ ]:


len(low_accident_cities)


# In[ ]:


sns.distplot(high_accident_cities)


# In[ ]:


sns.distplot(low_accident_cities)


# In[ ]:


sns.histplot(high_accident_cities,log_scale=True)


# In[ ]:


cities_by_accident[cities_by_accident==1]


# # Start time 

# In[ ]:


df.Start_Time


# In[ ]:


df.Start_Time[0]


# In[ ]:


df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')


# In[ ]:


df["Start_Time"]


# In[ ]:


df.Start_Time[0]


# In[ ]:


df.Start_Time.dt.hour


# In[ ]:


sns.histplot(df.Start_Time.dt.hour,bins=24)


# In[ ]:


# A high percntage of accidents occur between 6 am to 9 am and 3 pm to 7 pm probably people hurry to get to work


# In[ ]:


sns.distplot(df.Start_Time.dt.hour,bins=24,kde=False,norm_hist=True)


# In[ ]:


# on weekends no.of accidents are low


# In[ ]:


sns.distplot(df.Start_Time.dt.dayofweek,bins=7,kde=False,norm_hist=True)


# In[ ]:


# on weekends which time most accidents are occuring ( it seems that at afternoon more accidents are happening)


# In[ ]:


sundays_start_time=df.Start_Time[df.Start_Time.dt.dayofweek==6]


# In[ ]:


sns.distplot(sundays_start_time.dt.hour,bins=7,kde=False,norm_hist=True)


# In[ ]:


mondays_start_time=df.Start_Time[df.Start_Time.dt.dayofweek==0]
sns.distplot(mondays_start_time.dt.hour,bins=24,kde=False,norm_hist=True)


# In[ ]:


# more no.of accidents in the months of winter, less in summer and rainy. 


# In[ ]:


sns.distplot(mondays_start_time.dt.month,bins=12,kde=False,norm_hist=True)


# In[ ]:


df_2016=df[df.Start_Time.dt.year==2016]
sns.distplot(df_2016.Start_Time.dt.month,bins=12,kde=False,norm_hist=True)


# In[ ]:


df_2017=df[df.Start_Time.dt.year==2017]
sns.distplot(df_2017.Start_Time.dt.month,bins=12,kde=False,norm_hist=True)


# In[ ]:


df_2018=df[df.Start_Time.dt.year==2018]
sns.distplot(df_2018.Start_Time.dt.month,bins=12,kde=False,norm_hist=True)


# In[ ]:


sns.distplot(df_2019.Start_Time.dt.month,bins=12,kde=False,norm_hist=True)


# In[ ]:


df_2020=df[df.Start_Time.dt.year==2020]
sns.distplot(df_2020.Start_Time.dt.month,bins=12,kde=False,norm_hist=True)


# In[ ]:


df.Source.value_counts().plot(kind="pie")


# In[ ]:


# start Latitude & Longitude


# In[ ]:


df.Start_Lat


# In[ ]:


df.Start_Lng


# In[ ]:


sns.scatterplot(x=df.Start_Lng,y=df.Start_Lat)
plt.show()


# In[ ]:


sample_df=df.sample(int(0.1 * len(df)))


# In[ ]:


sns.scatterplot(x=sample_df.Start_Lng, y=df.Start_Lat, size=0.001)
plt.show()


# # putting Scatterplot in a map

# In[ ]:


pip install folium


# In[ ]:


import folium


# In[ ]:


m = folium.Map(location=[latitude, longitude], zoom_start=12)


# In[ ]:


lat,lng=df.Start_Lat[0],df.Start_Lng[0]
lat,lng


# In[ ]:


for x in df[["Start_Lat", "Start_Lng"]].sample(100).iteritems():
    print(x)


# In[ ]:


G_map = folium.Map()
marker = folium.Marker((lat,lng))
marker.add_to(G_map)
G_map


# In[ ]:




