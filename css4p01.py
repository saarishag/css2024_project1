"""
CSS Project - Option 1: IMDB Data

@author: Saarisha Govender
"""

"""
ETL

Loading and Cleaning Data
Renaming column names to remove spaces
Changing year column to datetime datatype

"""

import pandas as pd
df = pd.read_csv("movie_dataset.csv")

df.rename(columns={"Runtime (Minutes)":"runtime_minutes"}, inplace = True)
df.rename(columns={"Revenue (Millions)":"revenue_millions"}, inplace = True)

df["Year"] = pd.to_datetime(df["Year"], format="%Y")
df["Year"] = df["Year"].dt.year

"""
Filling NaNs with the mean of the columns
"""


x = df["revenue_millions"].mean()
df["revenue_millions"] = df["revenue_millions"].fillna(x)

y = round(df["Metascore"].mean())
df["Metascore"] = df["Metascore"].fillna(x)



"""
EDA
"""

#Question 1
print(df[df["Rating"]==max(df["Rating"])])
########################################################


#Question 2
avg_rev = (df["revenue_millions"].mean())
#82.95637614678898
#print(df.describe())
########################################################

#Question 3
#max_year = max(df['Year'])
avg_2_years =  df['revenue_millions'][df['Year'] >= 2015].mean() #can use >= since max(year)=2016
#68.06402328198025
##########################################################

#Question 4
grouped = df.groupby('Year')
count_titles = grouped['Title'].count()
print(count_titles) # 2016   297
########################################################

#Question 5
grouped = df.groupby("Director")
count_chris = grouped['Title'].count()
print(count_chris) #5
########################################################

#Question 6
high_rating = df['Title'][df["Rating"] >= 8.0].count()
print(high_rating) #78
########################################################

#Question 7
print(df['Rating'][df['Director'] == "Christopher Nolan"].median()) #8.6

"""
print(df['Rating'][df['Director'] == "Christopher Nolan"])
64     8.5
124    8.5
36     8.6
80     8.8
54     9.0
"""
########################################################

#Question 8
grouped = df.groupby('Year')
avg_year = grouped['Rating'].mean()
highest_avg_rating = max(avg_year)
print(highest_avg_rating) #7.133962264150944  2007
########################################################

#Question 9
count_2006 = df['Title'][df['Year'] == 2006].count() #44
count_2016 = df['Title'][df['Year'] == 2016].count() #297

incr = count_2016 - count_2006
perc_incr = (incr/count_2006)*100
print(perc_incr) #575%
#####################################################

#Question 10
actor_df = df['Actors'].str.split(',')
#explode the lists
actor_df = actor_df.explode('Actors')

#to get rid of counting issues due to trailing and leading blank spaces 
actor_df = actor_df.str.replace(" ", "")
actor_counts = actor_df.value_counts() #Mark Wahlberg  15
####################################################

#Question 11
genre_df = df['Genre'].str.split(",")
genre_df = genre_df.explode('Genre') 
genre_counts = genre_df.value_counts()
print(genre_df.value_counts().count()) #20 
########################################################33

#Question 12
import matplotlib.pyplot as plt
plt.scatter(df['Votes'], df['revenue_millions'])
plt.xlabel("Votes")
plt.ylabel("Revenue (Millions)")
plt.show()

plt.bar(df['revenue_millions'], df['Votes'])
plt.ylabel("Votes")
plt.xlabel("Revenue (Millions)")
plt.show()

plt.bar(df['Rating'], df['revenue_millions'])
plt.xlabel("Rating")
plt.ylabel("Revenue (Millions)")
plt.show()

plt.bar(df['Metascore'], df['revenue_millions'])
plt.xlabel("Metascore")
plt.ylabel("Revenue (Millions)")
plt.show()

plt.bar(df['runtime_minutes'], df['revenue_millions'])
plt.xlabel("runtime_minutes")
plt.ylabel("Revenue (Millions)")
plt.show()

plt.bar(df['Year'], df['Votes'])
plt.xlabel("Year")
plt.ylabel("Votes")
plt.show()

plt.bar(df['Year'], df['Rating'])
plt.xlabel("Year")
plt.ylabel("Rating")
plt.show()

plt.bar(df['Year'], df['Metascore'])
plt.xlabel("Year")
plt.ylabel("Metascore")
plt.show()

#Pandas Profiling used for the rest of the insights
from ydata_profiling import ProfileReport

profile = ProfileReport(df, title = "Profiling Report")

profile.to_file("your_project_report.html")














