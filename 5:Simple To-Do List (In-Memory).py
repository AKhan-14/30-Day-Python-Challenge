# The Challenge: Create a command-line to-do list application where a user can add a task, 
# view all tasks, and mark a task as complete (remove it from the list). 
# The list is forgotten when the program closes.

# Step 1: The Foundation - Storing Your Tasks

"""

to_do_list = []
print(to_do_list)

"""


# Step 2: The Engine - The Main Application Loop

"""

to_do_list = []
# print(to_do_list)

while True:
    command = input("What would you like to do? ")
    if command == "quit" or command == "q":
        break
    else:
        print("That is NOT a valid command, try again. ")
        continue

"""

# Step 3: The First Command - "view"

"""

to_do_list = ["Train hard","Eat whole natural foods"]
# print(to_do_list)

while True:
    command = input("What would you like to do? ")
    if command == "quit" or command == "q":
        break
    elif command == "view" or command == "v":
        if to_do_list == []:
            print("The list is empty. ")
        else:
            for items in to_do_list:
                print(items)
    else:
        print("That is NOT a valid command, try again. ")
        continue
        
"""

# Step 4: The Second Command - "add"

"""

to_do_list = []
# print(to_do_list)

while True:
    command = input("What would you like to do? ")
    if command == "quit" or command == "q":
        break
    elif command == "view" or command == "v":
        if to_do_list == []:
            print("The list is empty. ")
        else:
            for items in to_do_list:
                print(items)
    elif command == "add" or command == "a":
        new_item = input("Add a new task: ")
        to_do_list.append(new_item)
        print(f"Nice! You have added '{new_item}' to the to do list. ")
    else:
        print("That is NOT a valid command, try again. ")
        continue

"""

# Step 5: The Third Command - "remove" (The Real Challenge)

to_do_list = ["Train hard", "Eat whole natural foods"]
# print(to_do_list)

while True:
    command = input("What would you like to do? ")
    if command == "quit" or command == "q":
        break
    elif command == "view" or command == "v":
        if to_do_list == []:
            print("The list is empty. ")
        else:
            print("Your To-Do List:")
            for index, tasks in enumerate(to_do_list, start=1):
                print(f"{index}. {tasks}")
    elif command == "add" or command == "a":
        new_item = input("Add a new task: ")
        to_do_list.append(new_item)
        print(f"Nice! You have added '{new_item}' to the list. ")
    elif command == "remove" or command == "r":
        while True:
            remove_item = input("Which task would you like to remove? ")
            if remove_item == "None":
                print("No tasks were removed. ")
                break
            try:
                remove_item = int(remove_item) - 1
                if 0 <= remove_item < len(to_do_list):
                    print(f"You have successfully removed '{to_do_list.pop(remove_item)}' from the list. ")
                    break
                else:
                    print(f"The list is only {len(to_do_list)} task(s) long buddy, not {remove_item + 1}. ")
            except ValueError:
                print("That is not a number. Try again")
    else:
        print("That is NOT a valid command, try again. ")
        continue