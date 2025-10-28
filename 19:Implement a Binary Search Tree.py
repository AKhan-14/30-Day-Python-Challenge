# The Challenge: Implement a basic Binary Search Tree (BST) from scratch. 
# It should have an insert method and a search method.
# The BST Rule: For any given node in the tree:
# All values in its left subtree are less than its own value.
# All values in its right subtree are greater than its own value.

# Step 1: The Node Class (The Building Block)

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

# Step 2: The BinarySearchTree Class (The Container)

class BinarySearchTree:
    def __init__(self):
        self.root = None

# Step 3: The insert Method (The Core Recursive Logic)

    def insert(self,value):
        if self.root == None:
            self.root = Node(value)
        elif self.root != None:
            self._insert_recursive(self.root,value)
    
    def _insert_recursive(self,current_node,value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left,value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            elif current_node.right != None:
                return self._insert_recursive(current_node.right,value)
        elif value == current_node.value:
            return

# Step 4: The search Method (The Payoff)
    
    def search(self,value):
        return self._search_recursive(self.root,value)
    
    def _search_recursive(self,current_node,value):
        if current_node == None:
            return False
        elif value == current_node.value:
            return True
        elif value < current_node.value:
            return self._search_recursive(current_node.left,value)
        elif value > current_node.value:
            return self._search_recursive(current_node.right,value)
 

my_tree = BinarySearchTree()
my_tree.insert(10)
my_tree.insert(5)
print(my_tree.search(10))
print(my_tree.search(7))
