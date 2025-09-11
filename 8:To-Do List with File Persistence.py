import json
# Week 2: Interacting with the Outside World
# The Challenge: Upgrade your Day 5 To-Do list. 
# When the program starts, it should load any existing tasks from a file. 
# When a task is added or removed, it should save the updated list back to the file.

# Day 5 To do list
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

# Step 1: The save_tasks Function
# with open('tasks.json', 'w') as file:
#     json.dump(to_do_list, file)

def save_tasks(tasks_to_save): 
    with open('tasks.json', 'w') as file:
        json.dump(tasks_to_save, file)

# Step 2: The load_tasks Function
# try:
#     with open('tasks.json') as file:
#         full_text = json.load(file)
#         print(full_text)
# except:
#     print("Error: 'tasks.json' not found. Make sure its in the same folder as your script.")

def load_tasks(): 
    try:
        with open('tasks.json', 'r') as file: 
            return json.load(file) 
    except FileNotFoundError:
        return []