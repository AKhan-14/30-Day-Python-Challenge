# The Challenge: Represent a maze as a 2D grid (a list of lists). 
# Write a function that finds a path from a start 'S' to an end 'E', avoiding walls '#'.

# Step 1: The Setup - Representing the Maze
# The BFS Analogy: Spreading Ink
# Imagine you drop a blob of ink at the "S" (start) position. 
# In the first second, the ink spreads to all adjacent, open squares. 
# In the second second, it spreads from all of those squares to their adjacent, open squares. B
# FS explores the graph in expanding concentric circles, layer by layer. 
# This is why it is guaranteed to find the shortest path.

# The Frontier (The Core of BFS): Queue Class
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,item):
        self.queue.append(item)
    
    def dequeue(self):
        if self.queue == []:
            return None
        else:
            return self.queue.pop(0)
        
    def is_empty(self):
        if self.queue == []:
            return True
        else:
            return False
    
    def size(self):
        return len(self.queue)
    
    def front(self):
        if self.queue == []:
            return None
        else:
            return self.queue[0]

# Sample Maze
# 'S': This is the Start point. It's the coordinate where your search begins.
# 'E': This is the End point. It's the coordinate your algorithm is trying to reach.
# '#': This is a Wall. It represents an obstacle. Your algorithm is not allowed to move into a cell that contains a wall.
# ' ' (a space): open path or a "corridor". These are the valid cells your algorithm can move through.
maze = [
    ["#", "#", "#", "#", "#", "S", "#"],
    ["#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", "E", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#"]
]
        
# Step 1: The Setup
def solve_maze(maze_grid):
# The Starting Point: 'S'
    start_pos = None
    for i in range(len(maze_grid)):
        for j in range(len(maze_grid[i])):
            if maze_grid[i][j] == "S":
                start_pos = (i, j)
                # print(start_pos)
                break

    # Create data structures
    frontier = Queue()
    visited = set()

# Step 2: Initialize the Search
    if start_pos:
        visited.add(start_pos)
        start_path = [start_pos] # Item is a path, list of coordinates
        frontier.enqueue(start_pos)

# Step 3: The Main Loop and The "Goal Test"
    while not frontier.is_empty():
        current_path = frontier.dequeue()
        current_pos = current_path[-1]
        row, col = current_pos
        if maze_grid[row][col] == "E":
            return current_path

# Step 4: Finding and Adding Neighbors      
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for move in moves:
            next_row = row + move[0], next_col = col + move[1]