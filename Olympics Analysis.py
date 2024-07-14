#!/usr/bin/env python
# coding: utf-8

# # Importing the libraries

# In[1]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# # Loading the data

# In[2]:


df=pd.read_excel("D:\\dataset_olympics.xlsx")
df.head()


# In[3]:


df.info()


# In[4]:


df.describe()


# In[5]:


df.describe(include=["object"])


# In[6]:


df.isnull().sum()


# In[7]:


df.duplicated().sum()


# In[8]:


df.drop_duplicates(inplace=True)


# In[9]:


df.duplicated().sum()


# # Exploratory Data Analysis

# In[10]:


sns.countplot(x=df["Sex"])
plt.title("Gender Distribution")
plt.show()


# In[11]:


sns.histplot(df["Age"],bins=10,kde=True)
plt.title("Age Distribution")
plt.show()


# In[12]:


sns.histplot(df["Height"],bins=20,kde=True)
plt.title("Height Distribution")
plt.show()


# In[13]:


sns.histplot(df["Weight"],bins=20,kde=True)
plt.title("Weight Distribution")
plt.show()


# In[14]:


sns.countplot(x=df["Medal"])
plt.title("Medal Distribution")
plt.show()


# In[15]:


sns.countplot(data=df, x="Year",hue="Medal")
plt.title("Medal Distribution Over Year")
plt.xticks(rotation=45)
plt.show()


# In[16]:


year_avg_age=df.groupby("Year")["Age"].mean()
print(year_avg_age)


# In[17]:


sport_median_height=df.groupby("Sport")["Height"].median()
print(sport_median_height)
print(sport_median_height.max())
print(sport_median_height.min())


# In[18]:


sport_median_height[sport_median_height==190.0]


# In[19]:


sport_median_height[sport_median_height==164.0]


# In[20]:


country_gender_count=df.groupby(["NOC","Sex"])["ID"].count()
print(country_gender_count)


# In[21]:


country_gold_medals=df[df["Medal"]=="Gold"].groupby("NOC")["Medal"].count()
print(country_gold_medals)


# In[22]:


print(country_gold_medals.max())
print(country_gold_medals.min())


# In[23]:


country_gold_medals[country_gold_medals==747]
country_gold_medals[country_gold_medals==1]


# In[24]:


sport_gender_avg_weight=df.groupby(["Sport","Sex"])["Weight"].mean()
print(sport_gender_avg_weight)


# In[25]:


sport_event_count=df.groupby("Sport")["Event"].nunique().sort_values(ascending=False)
sport_event_count.plot(kind="bar")
plt.title("no.of unique events per sport")
plt.xlabel("sport")
plt.ylabel("no.of unique events")
plt.xticks(rotation=45)
plt.show()


# In[26]:


year_participation_count=df.groupby("Year")["ID"].nunique()
year_participation_count.plot(kind="bar")
plt.title("no.of participation over the years")
plt.xlabel("year")
plt.ylabel("no.of participants")
plt.show()


# In[27]:


country_avg_age=df.groupby("NOC")["Age"].mean().sort_values(ascending=False)
country_avg_age.head(10).plot(kind="bar")
plt.title("Top 10 countries with highest average age of participation")
plt.xlabel("country")
plt.ylabel("Average Age")
plt.xticks(rotation=45)
plt.show()


# In[28]:


country_avg_age=df.groupby("NOC")["Age"].mean().sort_values(ascending=False)
country_avg_age.tail(10).plot(kind="bar")
plt.title("Top 10 countries with lowest average age of participation")
plt.xlabel("country")
plt.ylabel("Average Age")
plt.xticks(rotation=45)
plt.show()


# In[29]:


sns.boxplot(x=df["Season"],y=df["Age"])
plt.title('Distributions of ages by seasons')
plt.xlabel("season")
plt.ylabel("Age")
plt.show()


# In[30]:


sns.violinplot(data=df,x="Medal",y="Height",palette="Set2")
plt.title("distribution og medals by heights")
plt.xlabel("Medal")
plt.ylabel("Height")
plt.show()


# In[31]:


most_medals_country=df["NOC"].value_counts().idxmax()
print("most medal winning country:",most_medals_country)


# In[32]:


tallest_athlete= df[df["Height"]==df["Height"].max()]
print("tallest_athlete")
print(tallest_athlete[["ID","Name","Height","Sport"]])


# In[33]:


shortest_athlete= df[df["Height"]==df["Height"].min()]
print("shortest_athlete")
print(shortest_athlete[["ID","Name","Height","Sport"]])


# In[34]:


heaviest_athlete= df[df["Weight"]==df["Weight"].max()]
print("heaviest_athlete")
print(heaviest_athlete[["ID","Name","Height","Sport"]])


# In[35]:


heaviest_athlete= df[df["Weight"]==df["Weight"].min()]
print("heaviest_athlete")
print(heaviest_athlete[["ID","Name","Height","Sport"]])


# In[36]:


sns.scatterplot(data=df,x="Height",y="Weight",hue="Medal",palette="Set1")
plt.title("Athlete Height vs Weight by medal status")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.legend(title="Medal")
plt.show()


# In[ ]:




