# Week 1: Core Logic and Foundational Structures
# The Challenge: Write a program that asks for the user's name and their favorite color, 
# and then prints a message like, "Hello [Name], I see your favorite color is [Color]. 
# That's a great choice!"

full_name = input("What is your full name? ")
# print(full_name)
if full_name.isalpha() == True:
    print(full_name)
else:
    while full_name.isalpha() == False:
        print("Your name can only include letters, Try Again")
        full_name = input("What is your full name? ")
        continue

colour_list = ["red","blue","yellow"]
fav_colour = input("What is your favourite primary colour? ")
# print(fav_colour)
if fav_colour.lower() in colour_list:
    print(fav_colour)
else:
    while fav_colour.lower() not in colour_list:
        print("That is not a primary colour, Try Again")
        fav_colour = input("What is your favourite primary colour? ")
        continue

number = input("Pick a number? ")
# print(number)
if number.isdigit() == True:
    print(number)
else:
    while number.isdigit() == False:
        print("Your number can only include whole digits, Try Again")
        number = input("Pick a number? ")
        continue

# print("Hello {}, I see your favourite color is {}. That's a great choice!".format(full_name, fav_colour))
print(f"Hello {full_name}, I see your favourite primary colour is {fav_colour.lower()} and chosen number is {number}. That's a great choice!")


