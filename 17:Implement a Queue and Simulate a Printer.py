# The Challenge: Implement a Queue class from scratch. 
# Then, create a simple simulation where "print jobs" are added to a queue 
# and a "printer" processes them one by one in the order they were received.

# Part 1: Building the Queue Class

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
        
class PrintJob:
    def __init__(self,name,pages):
        self.name = name
        self.pages = pages

# Part 2: The Printer Simulation

# Step 1: The Setup
import time
import random 

printer_queue = Queue()
current_job = None
time_remaining = 0
time_per_page = 2

total_simulation_time = 30

for second in range(1, total_simulation_time + 1):
    print(f"--- Second {second} ---")
    possibility_of_new_job = random.randint(0,5)
    if possibility_of_new_job == 1:
        new_job = PrintJob(f"Job_{second}",random.randint(0,10))
        printer_queue.enqueue(new_job)

    if current_job is None and not printer_queue.is_empty():
        current_job = printer_queue.dequeue()
        time_remaining = current_job.pages * time_per_page
        print(f"ACTION: Printer started job '{current_job.name}'. Will take {time_remaining} seconds.")

    if current_job is not None:
        time_remaining -= 1
        print(f"STATUS: Printer is working on '{current_job.name}'. {time_remaining} seconds left.")
        if time_remaining <= 0:
            print(f"EVENT: Printer FINISHED job '{current_job.name}'.")

            current_job = None

    else:
        print("STATUS: Printer is idle.")
        
    print(f"QUEUE: {printer_queue.size()} jobs waiting.")
    print("-" * 20)
    time.sleep(1)
        
            

        

    
