# The Challenge: Create a program that takes two numbers and an operator (+, -, *, /) 
# from the user and performs the calculation.

# Step 1: The "Happy Path" - The Simplest Working Version

"""

first_number = input("Give me your first number: ")
if first_number.isdigit() == True:
    print(first_number)
else:
    while first_number.isdigit() == False:
        print("Your number can only include whole digits, Try Again")
        first_number = input("Give me your first number, again: ")
        continue
print(f"Your first number is {first_number}")

second_number = input("Give me your second number: ")
if second_number.isdigit() == True:
    print(second_number)
else:
    while second_number.isdigit() == False:
        print("Your number can only include whole digits, Try Again")
        second_number = input("Give me your second number, again: ")
        continue
print(f"Your first number is {second_number}")

operator_list = ["+", "-", "*", "/", "add", "subtract", "multiply", "times", "divide"]
operator = input("What is your operator? ")
if operator.lower() in operator_list:
    print(operator)
else:
    while operator.lower() not in operator_list:
        print("That is not an operator, Try Again")
        operator = input("What is your operator? ")
        continue
final_answer = 0
if operator == "+" or operator == "add":
    final_answer = (float(first_number) + float(second_number))
    print(f"Answer: {first_number} + {second_number} = {final_answer}")
elif operator == "-" or operator == "subtract":
    final_answer = (int(first_number) - int(second_number))
    print(f"Answer: {first_number} - {second_number} = {final_answer}")
elif operator == "*" or operator == "multiply" or operator == "times":
    final_answer = (int(first_number) * int(second_number))
    print(f"Answer: {first_number} * {second_number} = {final_answer}")
else:
    final_answer = (int(first_number) / int(second_number))
    print(f"Answer: {first_number} / {second_number} = {final_answer}")

"""

# Step 2: Refactoring into Functions 

"""

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

first_number = input("Give me your first number: ")
if first_number.isdigit() == True:
    print(first_number)
else:
    while first_number.isdigit() == False:
        print("Your number can only include whole digits, Try Again")
        first_number = input("Give me your first number, again: ")
        continue
print(f"Your first number is {first_number}")

second_number = input("Give me your second number: ")
if second_number.isdigit() == True:
    print(second_number)
else:
    while second_number.isdigit() == False:
        print("Your number can only include whole digits, Try Again")
        second_number = input("Give me your second number, again: ")
        continue
print(f"Your first number is {second_number}")

operator = input("What is your operator? ")
final_answer = 0
if operator == "+" or operator == "add":
    final_answer = (add(float(first_number),float(second_number)))
    print(f"Answer: {first_number} + {second_number} = {final_answer}")
elif operator == "-" or operator == "subtract":
    final_answer = (subtract(float(first_number),float(second_number)))
    print(f"Answer: {first_number} - {second_number} = {final_answer}")
elif operator == "*" or operator == "multiply" or operator == "times":
    final_answer = (multiply(float(first_number),float(second_number)))
    print(f"Answer: {first_number} * {second_number} = {final_answer}")
else:
    final_answer = (divide(float(first_number),float(second_number)))
    print(f"Answer: {first_number} / {second_number} = {final_answer}")

"""

# Step 3: Graceful Input Validation

"""

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

while True:
    first_number = input("Give me your first number: ")
    try:
        # Try to convert the input string to a floating-point number
        first_number = float(first_number)
        # If the line above works, we break the loop
        break
    except ValueError:
        # If the line above fails, it raises a ValueError, which we catch here.
        print("That's not a valid number. Please try again.")

while True:
    second_number = input("Enter the second number: ")
    try:
        second_number = float(second_number)
        break
    except ValueError:
        print("That's not a valid number. Please try again.")

operator_list = ["+", "-", "*", "/", "add", "subtract", "multiply", "times", "divide"]
while True:
    operator = input("What is your operator? ")
    if operator.lower() in operator_list:
        break
    else:
        print("That's not a valid operator. Please try again.")

final_answer = 0
if operator == "+" or operator == "add":
    final_answer = (add((first_number),(second_number)))
    print(f"Answer: {first_number} + {second_number} = {final_answer}")
elif operator == "-" or operator == "subtract":
    final_answer = (subtract((first_number),(second_number)))
    print(f"Answer: {first_number} - {second_number} = {final_answer}")
elif operator == "*" or operator == "multiply" or operator == "times":
    final_answer = (multiply((first_number),(second_number)))
    print(f"Answer: {first_number} * {second_number} = {final_answer}")
else:
    final_answer = (divide((first_number),(second_number)))
    print(f"Answer: {first_number} / {second_number} = {final_answer}")

"""

# Step 4: Handling the Division-by-Zero Edge Case

"""

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero!"
    else:
        return num1 / num2

while True:
    first_number = input("Give me your first number: ")
    try:
        # Try to convert the input string to a floating-point number
        first_number = float(first_number)
        # If the line above works, we break the loop
        break
    except ValueError:
        # If the line above fails, it raises a ValueError, which we catch here.
        print("That's not a valid number. Please try again.")

while True:
    second_number = input("Enter the second number: ")
    try:
        second_number = float(second_number)
        break
    except ValueError:
        print("That's not a valid number. Please try again.")

operator_list = ["+", "-", "*", "/", "add", "subtract", "multiply", "times", "divide"]
while True:
    operator = input("What is your operator? ")
    if operator.lower() in operator_list:
        break
    else:
        print("That's not a valid operator. Please try again.")

final_answer = 0
if operator == "+" or operator == "add":
    final_answer = (add((first_number),(second_number)))
    print(f"Answer: {first_number} + {second_number} = {final_answer}")
elif operator == "-" or operator == "subtract":
    final_answer = (subtract((first_number),(second_number)))
    print(f"Answer: {first_number} - {second_number} = {final_answer}")
elif operator == "*" or operator == "multiply" or operator == "times":
    final_answer = (multiply((first_number),(second_number)))
    print(f"Answer: {first_number} * {second_number} = {final_answer}")
else:
    final_answer = (divide((first_number),(second_number)))
    print(f"Answer: {first_number} / {second_number} = {final_answer}")

"""

# Step 5: The Main Loop

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero!"
    else:
        return num1 / num2
    
while True:
    while True:
        first_number = input("Give me your first number: ")
        try:
            # Try to convert the input string to a floating-point number
            first_number = float(first_number)
            # If the line above works, we break the loop
            break
        except ValueError:
            # If the line above fails, it raises a ValueError, which we catch here.
            print("That's not a valid number. Please try again.")

    while True:
        second_number = input("Enter the second number: ")
        try:
            second_number = float(second_number)
            break
        except ValueError:
            print("That's not a valid number. Please try again.")

    operator_list = ["+", "-", "*", "/", "add", "subtract", "multiply", "times", "divide"]
    while True:
        operator = input("What is your operator? ")
        if operator.lower() in operator_list:
            break
        else:
            print("That's not a valid operator. Please try again.")

    final_answer = 0
    if operator == "+" or operator == "add":
        final_answer = (add((first_number),(second_number)))
        print(f"Answer: {first_number} + {second_number} = {final_answer}")
    elif operator == "-" or operator == "subtract":
        final_answer = (subtract((first_number),(second_number)))
        print(f"Answer: {first_number} - {second_number} = {final_answer}")
    elif operator == "*" or operator == "multiply" or operator == "times":
        final_answer = (multiply((first_number),(second_number)))
        print(f"Answer: {first_number} * {second_number} = {final_answer}")
    elif operator == "/" or operator == "divide":
        final_answer = (divide((first_number),(second_number)))
        print(f"Answer: {first_number} / {second_number} = {final_answer}")
    
    repeat = input("Would you like to do another calculation, Y/N? ")
    if repeat.lower() == "yes" or repeat.lower() == "y":
        continue
    elif repeat.lower() == "no" or repeat.lower() == "n":
        print("Thanks for using the calculator!")
        break
    else:
        print("That's not a valid answer. Please try again.")
        repeat = input("Would you like to do another calculation, Y/N? ")
