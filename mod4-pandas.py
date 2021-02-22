# Pandas: a popular library for data analysis
## My Watson Studio Lab: 

import pandas as pd

# dataframe: is comprised of rows amd columns. we can create a data frame out of a dictionary

csv_data_frame = pd.read_csv("resources/ex4.csv")
print(csv_data_frame.head())

xlsx_data_frame = pd.read_excel("resources/out.xlsx")
print(xlsx_data_frame.head())


# dictionary to dataframe
df=pd.DataFrame({'a':[11,91,31,23,34,45,45,56,67,67,78,45],'b':[21,22,23,34,34,56,67,78,34,56,67,78],'c':[21,22,23,34,34,56,67,78,34,56,67,78]})
print("### dictionary to dataframe")
print(df.head())

# select multiple columns
print("### select multiple columns")
print(df[['b', 'c']])

# select items
print("### select items df[row:column]")
print(df.iloc[1,1])

# select unique from a column
print("### select unique from a column")
print(df['a'].unique())

# find out the number equal to and grated than x
print("### find out the number equal to and grated than x")
print(df['a'] >= 20)

# find out the number equal to and grated than x and create a dataframe out of it
print("### find out the number equal to and grated than x and create a dataframe out of it")
df1 = df[df['a'] >= 30]
print(df1)

# saving a dataframe to a CSV file
df1.to_csv('resources/new_items.csv')
print("### saved a dataframe to a CSV file -> resources/new_items.csv")