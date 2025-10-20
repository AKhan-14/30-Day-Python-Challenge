# The Challenge: Implement a Linked List data structure from scratch. 
# Do not use your language's built-in list. 
# You will need a Node class and a LinkedList class. 
# Implement methods for append, prepend, and delete.

# Step 1: The Building Block - The Node Class

"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
"""

# Step 2: The Container - The LinkedList Class

"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
"""

# Step 3: CREATE (Part 1) - The append Method

"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next

        last_node.next = new_node
"""

# Step 4: A Helper Method - Displaying the List

"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next

        last_node.next = new_node
    
    def display(self):
        current_node = self.head
        elements = []
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
        print(elements)
"""

# Step 5: CREATE (Part 2) - The prepend Method

"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next

        last_node.next = new_node
    
    def display(self):
        current_node = self.head
        elements = []
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
        print(elements)

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
"""

# Step 6: The delete Method (The Real Challenge)

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next

        last_node.next = new_node
    
    def display(self):
        current_node = self.head
        elements = []
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
        print(elements)

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self,data):
        current_node = self.head
        previous_node = None

        # Empty list
        if not self.head:
            return
        
        # If it is a head node
        if data == self.head.data:
            self.head = self.head.next
            return
        
        while current_node is not None and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next
        if current_node != None:
            previous_node.next = current_node.next
        

my_list = LinkedList()

my_list.append("A")
my_list.append("B")
my_list.display()
my_list.prepend("D")
my_list.display()
my_list.delete("A")
my_list.display()