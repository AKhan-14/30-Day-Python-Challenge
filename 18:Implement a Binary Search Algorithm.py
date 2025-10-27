# The Challenge: Write a function that implements binary search. 
# It should take a sorted list and a target value, and return whether the value is in the list. 
# Do not use built-in search functions.

# Part 1: The Iterative Approach (Using a while loop)
# The Goal: Write a function, call it binary_search_iterative, 
# that takes two arguments: a sorted list of numbers (data) and a target value. 
# The function should return True if the target is in the list, and False if it is not.

def binary_search_iterative(data,target):
    low = 0
    high = len(data) - 1

    while (low <= high):
        mid = (low + high) // 2
        if target == data[mid]:
            # return "You found it!"
            return True
        elif target < data[mid]:
            high = mid - 1
        elif target > data[mid]:
            low = mid + 1

    # return "Target was not in the list!"
    return False

# Part 2: The Recursive Approach (Advanced Challenge)
# The Goal: Write a second function, binary_search_recursive, 
# that solves the same problem but using recursion. 
# Recursion is a function that calls itself. 
# This is a more advanced, but very elegant, computer science concept.

def binary_search_recursive(data,target, low, high):
    if low > high:
        return False
    mid = (low + high) // 2
    if target == data[mid]:
            return True
    elif target < data[mid]:
        return binary_search_recursive(data,target, low, mid - 1)
    elif target > data[mid]:
        return binary_search_recursive(data,target, mid + 1, high)