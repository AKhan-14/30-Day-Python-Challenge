# The Challenge: Find a simple CSV dataset online (e.g., Titanic dataset, Iris dataset). 
# Write a program that reads the data and calculates a simple statistic, 
# like the average age of passengers or the number of people in each class.

# Step 0: Setup - Get Your Data (iris.csv)

# Step 1: Reading the Raw Data
import csv

"""
with open ('iris.csv', 'r') as csvfile:
    # Create a reader object
    csv_reader = csv.reader(csvfile)

    # Iterate through the rows in the CSV file
    for row in csv_reader:
        # Access each element in the row
        print(row)
"""

# Step 2: Structuring the Data (The Most Important Step)

with open ('iris.csv', 'r') as csvfile:
    # Create a reader object
    csv_reader = csv.reader(csvfile)
    headers = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
    flowers = []

    # Iterate through the rows in the CSV file
    for row in csv_reader:
        # Access each element in the row
        # print(row)

        # Combine lists into dictionary using headers
        dictionary = dict(zip(headers, row))
        flowers.append(dictionary)

print(flowers)


