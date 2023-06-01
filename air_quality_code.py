# -*- coding: utf-8 -*-
"""
Created on Tue May 30 16:52:12 2023

@author: cladd
"""
import pandas as pd
# Load the dataset
data = pd.read_csv('annual_aqi_by_county_2022.csv')

# Print the first few rows of the dataset
print(data.head())
# Display detailed information about the DataFrame
print(data.info())

# Define a method to extract the number of days considered unhealthy in terms of air quality
def get_UnhealthyDays(item):
    return item['Unhealthy Days']
# Find the row with the minimum Unhealthy Days
min_row = min(data.iterrows(), key=lambda x: get_UnhealthyDays(x[1]))

# Access the values of the row
state = min_row[1]['State']
county = min_row[1]['County']
unhealthy_days = min_row[1]['Unhealthy Days']

# Print the result
print(f'The place with the minimum Unhealthy Days is: {state}, {county} ({unhealthy_days} Unhealthy Days)')

#Find the row with the maximum Unhealthy Days
max_row = max(data.iterrows(), key=lambda x: get_UnhealthyDays(x[1]))

# Access the values of the row
state = max_row[1]['State']
county = max_row[1]['County']
unhealthy_days = max_row[1]['Unhealthy Days']

# Print the result
print(f'The place with the maximum Unhealthy Days is: {state}, {county} ({unhealthy_days} Unhealthy Days)')


# Check if any county has more than 20 unhealthy days
has_more_than_20_days = any(data['Unhealthy Days'] > 10)

# Print the result
if has_more_than_20_days:
    print("There are counties with more than 10 unhealthy days.")
else:
    print("No counties have more than 10 unhealthy days.")

# Count the number of counties with more than 10 unhealthy days
count = sum(data['Unhealthy Days'] > 10)

# Print the result
print(f"There are {count} counties with more than 10 unhealthy days.")

# Filter the dataset to include only counties with more than 10 unhealthy days
filtered_data = data[data['Unhealthy Days'] > 10]

# Sort the filtered dataset by the "Unhealthy Days" column in descending order
sorted_data = filtered_data.sort_values(by='Unhealthy Days', ascending=False)

# Iterate over the sorted dataset and print the county and number of unhealthy days
for index, row in sorted_data.iterrows():
    county = row['County']
    unhealthy_days = row['Unhealthy Days']
    print(f"County: {county}, Unhealthy Days: {unhealthy_days}")







