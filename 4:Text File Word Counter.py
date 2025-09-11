# The Challenge: Write a program that reads a text file (.txt) 
# and counts the occurrences of each word. 
# It should then print the most common words.

# Step 0: Setup - Create Your Data File "sample.txt"

# Step 1: Reading the File

"""

try:
    with open ('sample.txt', 'r') as file:
        full_text = file.read()
        print(full_text)
except:
    print("Error: 'sample.txt' not found. Make sure its in the same folder as your script.")

"""

# Step 2: Normalizing and Splitting the Text

"""
try:
    with open ('sample.txt', 'r') as file:
        full_text = file.read()
        # print(full_text)
        # lowercase_text = full_text.lower()
        # print(lowercase_text)
        normalised_txt = full_text.replace('.', ' ')
        normalised_txt = normalised_txt.replace('?', ' ')
        # print(normalised_txt)
        split_normalised_txt = normalised_txt.split(' ')
        print(split_normalised_txt)
except:
    print("Error: 'sample.txt' not found. Make sure its in the same folder as your script.")

"""

# Step 3: Counting with a Dictionary

"""

try:
    with open ('sample.txt', 'r') as file:
        full_text = file.read()
        # print(full_text)
        # lowercase_text = full_text.lower()
        # print(lowercase_text)
        normalised_txt = full_text.replace('.', ' ')
        normalised_txt = normalised_txt.replace('?', ' ')
        # print(normalised_txt)
        word_list = normalised_txt.split(' ')
        # print(word_list)
except:
    print("Error: 'sample.txt' not found. Make sure its in the same folder as your script.")

word_counts = {}
for word in word_list:
    if word in word_counts:
        word_counts[word] = word_counts[word] + 1
    else:
        word_counts[word] = 1

# print(word_counts)

"""

# Step 4: Displaying the Most Common Words


try:
    with open ('sample.txt', 'r') as file:
        full_text = file.read()
        # print(full_text)
        # lowercase_text = full_text.lower()
        # print(lowercase_text)
        normalised_txt = full_text.replace('.', ' ')
        normalised_txt = normalised_txt.replace('?', ' ')
        # print(normalised_txt)
        word_list = normalised_txt.split(' ')
        # print(word_list)
except:
    print("Error: 'sample.txt' not found. Make sure its in the same folder as your script.")

word_counts = {}
for word in word_list:
    if word in word_counts:
        word_counts[word] = word_counts[word] + 1
    else:
        word_counts[word] = 1

# print(word_counts)
# print(word_counts.items())
sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)

for word, count in sorted_words[:5]:
    print(f"'{word}' appeared {count} times.")