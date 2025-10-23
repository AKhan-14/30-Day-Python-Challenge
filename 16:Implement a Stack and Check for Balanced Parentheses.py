# The Challenge: First, implement a Stack class from scratch. 
# Then, use your stack to write a function that checks if a string of parentheses (), brackets [], and braces {} is balanced. 
# E.g., "{[()]}" is balanced, but "{[(])}" is not.

# Step 1: Building Your Tool - The Stack Class

"""
class Stack:
    def __init__(self):
        self.stack = []

    def push(self,item):
        return self.stack.append(item)

    def pop(self):
        if self.stack == []:
            return self.stack.pop()
        else:
            return None
            #return ("Your list is empty")
    
    def top(self):
        if self.stack != []:
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        if self.stack == []:
            return True
        else:
            return False
    
    def size(self):
        return len(self.stack)
"""

# Step 2: The Algorithm - Planning the Parentheses Checker

# For "{[()]}" push, push, push, pop, pop, pop 

# Step 3: isBalanced class

class Stack:
    def __init__(self):
        self.stack = []

    def push(self,item):
        return self.stack.append(item)

    def pop(self):
        if self.stack == []:
            return None
            #return ("Your list is empty")
        else:
            return self.stack.pop()
            
    def top(self):
        if self.stack != []:
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        if self.stack == []:
            return True
        else:
            return False
    
    def size(self):
        return len(self.stack)
    
    def is_balanced(self,string):
        new_stack = Stack()
        opening_brackets = set(['(', '[', '{'])
        matched_pairs = {')': '(', ']': '[', '}': '{'}
        for char in string:
            if char in opening_brackets:
                new_stack.push(char)
            elif char in matched_pairs:
                if new_stack.is_empty():
                    return ("Oh No! Your string is inbalanced!")
                popped_item = new_stack.pop()
                popped_item_pair = matched_pairs[char]
                if popped_item != popped_item_pair:
                    return ("Oh No! Your string is inbalanced!")
        if new_stack.is_empty():
            return "Nice! The string is balanced!"
        else:
            return "Oh No! Your string is unbalanced!"

