# %%
# Project Name: Swiggy Restaurants Data Analysis

# Problem Statement:
# How many cities (including subregions) where Swiggy is having its restaurants listed?
# How many cities  (don't include subregions) where Swiggy is having their restaurants listed?
# The Subregion of Delhi with the maximum number of restaurants listed on Swiggy?
# Name the top 5 Most Expensive Cities in the Datasets.
# List out the top 5 Restaurants with Maximum & minimum ratings throughout the dataset.
# Name of top 5 cities with the highest number of restaurants listed.
# Top 10 cities as per the number of restaurants listed?
# Name the top 5 Most Popular Restaurants in Pune.
# Which SubRegion in Delhi is having the least expensive restaurant in terms of cost?
# Top 5 most popular restaurant chains in India?
# Which restaurant in Pune has the most number of people visiting?
# Top 10 Restaurants with Maximum Ratings in Banglore
# Top 10 Restaurant in Patna w.r.t rating 

# %%
# Import Data intodataframe 
import pandas as pd
import numpy as np

# %%
path=r"C:\Users\ankit\Downloads\GeeksForGeeksChallenge\data.json"
df_swiggy=pd.read_json(path)
df_swiggy.head(5)

# %%
df_swiggy['Delhi']['link']

# %%
df_swiggy.head(4)
df_new=df_swiggy.dropna(axis=0,how='all')
df_new.head(5)

# %%
df_new_updated=df_new.transpose()
df_new_updated.head(7)
# df_new_updated[~df_new_updated['restaurants'].isnull()]
print(df_new_updated.head(2))
df_new_updated=df_new_updated.reset_index()

# %%
df_new_updated.rename(columns={'index':'City'},inplace=True)

# %%
df_swiggy.shape

# %%
df_swiggy.columns

# %%
df_swiggy.isnull().sum()

# %%
df_non_null_swiggy=df_swiggy.copy()
# df_non_null_swiggy.dropna()

# %%
# How many cities (including subregions) where Swiggy is having its restaurants listed?
# How many cities  (don't include subregions) where Swiggy is having their restaurants listed?
df_non_null_swiggy=df_non_null_swiggy.transpose()
# df_non_null_swiggy.reset_index()

# %%
df_non_null_swiggy.head(4)

# %%
filter1=df_non_null_swiggy['restaurants'].isnull()

# %%
# How many cities (including subregions) where Swiggy is having its restaurants listed?
# How many cities  (don't include subregions) where Swiggy is having their restaurants listed?
len(df_non_null_swiggy[~df_non_null_swiggy['restaurants'].isnull()])

# %%
# 3.The Subregion of Delhi with the maximum number of restaurants listed on Swiggy?
df_new_updated['Old Delhi'].isnull().sum()

# %%
df_new_updated.info()

# %%
df_swiggy.columns

# %%
len(df_new_updated['restaurants'])
# df_new_updated[df_new_updated['restaurants'].str.contains('Aboh')]
df_new_updated.columns

# %%
df=pd.DataFrame()
for count, ele in enumerate(df_new_updated['restaurants']):
    print(count,ele)
    # df['ID'][count]=df_new_updated['restaurants'][count]
    # df['Name'][count]=df_new_updated['restaurants'][count][0]
    try:
        new_df=pd.DataFrame.from_dict(df_new_updated['restaurants'][count])
        x=df_new_updated['City'][count]
        new_df.to_json(f'temp_{count}_{x}.json', orient='columns')
    except Exception as e:
        print("Count:",count,e)
    

# %%
# len(df_new_updated['restaurants'])
# for index,value in enumerate(df_new_updated['restaurants'],len(df_new_updated)):
#     print(index,value)
#     if index==2:
#         break
    # new_df=pd.DataFrame()
    # new_df=pd.DataFrame.from_dict(df_new_updated['restaurants'][index])
    # new_df.to_json(f'temp{index}.json', orient='columns')



# %%
df_all=pd.DataFrame()
# df_all['All_Restaurants_Name']=df_new_updated['restaurants'].apply(lambda x:x)
new_df=pd.DataFrame()
new_df=pd.DataFrame.from_dict(df_new_updated['restaurants'][0])
# new_df=df_new_updated['restaurants'][0]
# df_new_updated['restaurants'][0]['567335']['name']
# df_new_updated['restaurants']

# %%
import glob

new_df.to_json('temp.json', orient='columns')
path2=r'C:\Users\ankit\Downloads\GeeksForGeeksChallenge\temp.json'
df_to=pd.read_json(path2)
transposed_df=df_to.transpose()
transposed_df=transposed_df.reset_index()
# transposed_df['City']


# %%
import os
import glob
final_dataframe = pd.DataFrame()

path_to_json = r'C:\Users\ankit\Downloads\GeeksForGeeksChallenge*' 

json_pattern = os.path.join(path_to_json,'*.json')
file_list = glob.glob(json_pattern)
print(file_list)

for file in file_list:
    print(file)

    city=file.split('_')[2]
    print(city)
    data = pd.read_json(file, lines=True)
    data=data.transpose()
    data=data.reset_index()
    data['City']=city
    final_dataframe = pd.concat([final_dataframe, data], ignore_index=True)
    # transposed_df_a1.append(transposed_df_a1, ignore_index = True)

# %%
final_dataframe['City'].unique().value_counts()

# %%
final_dataframe['City']=final_dataframe['City'].astype('str')
ser1=pd.Series(final_dataframe['City'])

# %%
final_dataframe


# %%
final_dataframe.rename(columns={0:"Data"},inplace=True)

# %%
import ast

new_dataframe = pd.DataFrame(final_dataframe['Data'].tolist())
new_dataframe

# %%
final_dataframe = pd.concat([final_dataframe, new_dataframe], axis=1)

# %%
final_dataframe['City']=final_dataframe['City'].apply(lambda x:x.split('.')[0])

# %%
final_dataframe.head(5)

# %%


# %%
# new_df.to_json()
new_df.to_json('temp.json', orient='columns')

# %%
path2=r'C:\Users\ankit\Downloads\GeeksForGeeksChallenge\temp.json'
df_to=pd.read_json(path2)

# %%
df_to

# %%
transposed_df=df_to.transpose()

# %%
transposed_df=transposed_df.reset_index()

# %%
print(transposed_df['address'][0])

# %%
transposed_df['City']=transposed_df['address'].apply(lambda x:x.split()[-1])

# %%
len(transposed_df)

# %%
transposed_df

# %%
df_new_updated[df_new_updated['City']=='Delhi']

# %%
df_new_updated['City'].str.contains('Del')

# %%
df_new_updated[df_new_updated['City'].str.contains('Del')]

# %%
# The Subregion of Delhi with the maximum number of restaurants listed on Swiggy?
delhi_link=df_new_updated[df_new_updated['City'].str.contains('Del')]['link']

# %%
# delhi_link.to

# %%
# df_delhi=pd.DataFrame(delhi_link)
df_delhi=pd.DataFrame.from_dict(df_new_updated['link'][162])

df_delhi

# %%
df_delhi=df_delhi.reset_index()

# %%
df_delhi['restaurants'][0]['link']

# %%
# df_delhi_restaurants=pd.DataFrame.from_dict(df_delhi['restaurants'])
# df_delhi_restaurants=df_delhi['restaurants'].apply(lambda z:z['link'])\
df_delhi_restaurants=pd.DataFrame(columns=['Restaurant'])
for count,value in enumerate(df_delhi['restaurants']):
    # _,data=value

    print("COunt",df_delhi['restaurants'][count]['link'])
    df_delhi_restaurants.loc[count]=df_delhi['restaurants'][count]['link']
    # df_delhi_restaurants['Restaurant'][count]=df_delhi['restaurants'][count]['link']


# %%
print(df_delhi_restaurants)

# %%
df_delhi_restaurants=df_delhi_restaurants['Restaurant'].apply(lambda x:x.split('-')[-4:-2])

# %%
x=pd.DataFrame(df_delhi_restaurants)

# %%
x

# %%
x['Restaurant']=x['Restaurant'].astype('str')

# %%
ser=pd.Series(x['Restaurant'])

# %%
ser.value_counts()

# %% [markdown]
# We can see Connaught Palace has the most number of restaurants listed in Delhi 

# %%
# Name the top 5 Most Expensive Cities in the Datasets.
# List out the top 5 Restaurants with Maximum & minimum ratings throughout the dataset.
# Name of top 5 cities with the highest number of restaurants listed.
# Top 10 cities as per the number of restaurants listed?
# Name the top 5 Most Popular Restaurants in Pune.
# Which SubRegion in Delhi is having the least expensive restaurant in terms of cost?
# Top 5 most popular restaurant chains in India?
# Which restaurant in Pune has the most number of people visiting?
# Top 10 Restaurants with Maximum Ratings in Banglore
# Top 10 Restaurant in Patna w.r.t rating 


# %%
# List out the top 5 Restaurants with Maximum & minimum ratings throughout the dataset.


# %%
ser1.value_counts()

# %%
# Name of top 5 cities with the highest number of restaurants listed.
# Bikaner,Sirsa,Sultanpur,Noida-1,Patna are the 5 citues with the highest number of restaurants Listed

# %%
final_dataframe.head(5)

# %%
# Top 10 cities as per the number of restaurants listed?
ser1.value_counts()[0:11]

# %%
# Name the top 5 Most Popular Restaurants in Pune.
df_pune=final_dataframe[final_dataframe['City']=='Pune']
df_pune
# Which SubRegion in Delhi is having the least expensive restaurant in terms of cost?
# Top 5 most popular restaurant chains in India?
# Which restaurant in Pune has the most number of people visiting?
# Top 10 Restaurants with Maximum Ratings in Banglore
# Top 10 Restaurant in Patna w.r.t rating 

# %%
new_dict=df_swiggy['Pune']['link']


# %%
new_dataframe_pune = pd.DataFrame(new_dict)
new_dataframe_pune['restaurants']

# %%
restaurants_Pune=pd.DataFrame(new_dataframe_pune['restaurants'].tolist())
restaurants_Pune

# %%
restaurants_Pune['rating'].value_counts()

# %%



