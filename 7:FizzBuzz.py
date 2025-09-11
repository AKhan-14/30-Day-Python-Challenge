#The Challenge: Write a program that prints numbers from 1 to 100. 
# But for multiples of three, print "Fizz" instead of the number. For the multiples of five, 
# print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".

# Step 1: The Scaffolding - Looping from 1 to 100

"""

for numbers in range(0,101):
    print(numbers)

"""

# Step 2: The Core Tool - Checking for Multiples
# Step 3: The Brain - The Conditional Logic
# Step 4: Assembly and Refinement

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz") 
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz") 
    else:
        print(number)
