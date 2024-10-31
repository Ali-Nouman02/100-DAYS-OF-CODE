import os
import csv
import pandas as pd

# os.chdir('C:\\Users\\Dell\\Desktop\\Data Science\\python')

# with open('weather_data.csv', 'r') as datafile:
#     content = csv.reader(datafile)
#     temp = []
#     print(f"this is csv file object{content}")
#     for row in content:
#         # print(row)
#         if row[1] != "temp":
#             temp.append(row[1])
# print("this is the list with all temps: ")
# print(temp)

# df = pd.read_csv("weather_data.csv")
# print(df)
# s = df.loc[:,"temp"]
# mean = s.mean()
# print(f"this is the mean {mean}")

#get a row from the dataframe through conditional formatting


# #goal is to print out the row where the temp is the max
# print(df[df.temp == df.temp.max()])

#goal get monday temp but convert it into Fahrenheit
# df_2 = df.loc[:, ['day','temp']]
# #give me the temp value where day is Monday
# monday = df[df.day == 'Monday']
# #this the temp on Monday
# temp = monday['temp']
# print(temp )
# #Celsius to Fahrenheit, multiply by 2 then add 30.
#
# f = (temp * 2) +30
# print(f)

df = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240816.csv')



