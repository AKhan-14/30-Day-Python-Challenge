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

"""
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
"""

# Step 3: Answering Your First Question: "What is the average sepal length for each species?"

"""
with open ('iris.csv', 'r') as csvfile:
    # Create a reader object
    csv_reader = csv.reader(csvfile)
    headers = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
    flowers = []

    # Iterate through the rows in the CSV file
    for row in csv_reader:
        # Access each element in the row
        # print(row)
        # check if the row is valid before processing.
        if row:
            # Combine lists into dictionary using headers
            dictionary = dict(zip(headers, row))
            flowers.append(dictionary)
    # print(flowers)

    # Grouping by 'species' using a for loop
    species_sepal_length_list = {}
    for flower in flowers:
        key = flower['species']
        if key not in species_sepal_length_list:
            species_sepal_length_list[key] = []
        species_sepal_length_list[key].append(float(flower['sepal_length']))
    
    for items in species_sepal_length_list.items():
        print(f"{items[0]} average is: {sum(items[1])/len(items[1])}")
"""

# Step 4: Answering a Second Question: "Which species has the largest petal?"

with open ('iris.csv', 'r') as csvfile:
    # Create a reader object
    csv_reader = csv.reader(csvfile)
    headers = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
    flowers = []

    # Iterate through the rows in the CSV file
    for row in csv_reader:
        # Access each element in the row
        # print(row)
        # check if the row is valid before processing.
        if row:
            # Combine lists into dictionary using headers
            dictionary = dict(zip(headers, row))
            flowers.append(dictionary)
    # print(flowers)

    largest_petal_area = 0.0
    record_holder_flower = None

    # Find 'petal_length' and 'petal_width'
    for flower in flowers:
        petal_length = flower['petal_length']
        petal_width = flower['petal_width']

        # Try convert string value into float
        try:
            petal_length = float(petal_length)
            petal_width = float(petal_width)
        except ValueError:
            print("That's not a valid number. Please try again.")
    
        # Calculations
        current_petal_area = petal_length * petal_width
        if current_petal_area > largest_petal_area:
            largest_petal_area = current_petal_area
            record_holder_flower = flower

    print(largest_petal_area)
    print(record_holder_flower)
