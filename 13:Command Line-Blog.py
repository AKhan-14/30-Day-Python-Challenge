# The Challenge: Create a command-line application that lets you write blog posts. 
# Each post should be saved as a separate file. 
# You should be able to create new posts, list all existing posts, and read a specific post.

# Step 1: The Foundation - The Blog "Database"

"""
import os
print(os.path.isdir("blog_posts"))
if not os.path.isdir("blog_posts"):
    os.mkdir("blog_posts")
    print("'blog_posts' directory successfully created.")
"""

# Step 2: The Engine - The Main Application Loop

import os
import time 

while True:
    command = input("What would you like to do? ")
    if command == "create" or command == "c":
        title = input("\nWhat is the title of your file? ")
        print("Title created successfully!")
        content = input("\nNow, write the content of your post: ")
        messy_title = title.lower().replace(' ', '_')
        safe_characters = "abcdefghijklmnopqrstuvwxyz0123456789_"
        safe_title = ""
        for character in messy_title:
            if character in safe_characters:
                safe_title = safe_title + character
            else:
                continue
        timestamp = str(int(time.time()))
        # print(timestamp)
        # print(safe_title)
        # print(os.getcwd())
        script_directory = os.path.dirname(__file__)
        posts_folder_name = "blog_posts"
        base_dir = os.path.join(script_directory,posts_folder_name)
        filename = f"{timestamp}_{safe_title}.txt"
        full_path = os.path.join(base_dir, filename)
        file_content = f"Title: {title}\n\nContent: {content}"
        with open(full_path, 'w') as f:
            f.write(file_content)
        print("Post created successfully!\n")

    elif command == "list" or command == "l":
        posts_folder_name = "blog_posts"
        script_dir = os.path.dirname(__file__)
        posts_dir = os.path.join(script_dir, posts_folder_name)
        # dir_list = os.listdir(posts_folder_name)
        # print(dir_list)
        try:
            dir_list = os.listdir(posts_dir)
            if not dir_list:
                print("No blog posts found.")
            else:
                print("\n--- Your Blog Posts ---")
            for index, filename in enumerate(dir_list, start=1):
                print(f"{index}. {filename}")
            print("\n")
        except FileNotFoundError:
            print("The blog_posts directory does not seem to exist yet. Create a post first.")
        
    elif command == "read" or command == "r":
        posts_folder_name = "blog_posts"
        script_dir = os.path.dirname(__file__)
        posts_dir = os.path.join(script_dir, posts_folder_name)
        # dir_list = os.listdir(posts_folder_name)
        # print(dir_list)
        try:
            dir_list = os.listdir(posts_dir)
            if not dir_list:
                print("No blog posts found.")
            else:
                print("\n--- Your Blog Posts ---")
            for index, filename in enumerate(dir_list, start=1):
                print(f"{index}. {filename}")
            print("\n")
        except FileNotFoundError:
            print("The blog_posts directory does not seem to exist yet. Create a post first.")
        
        while True:
            pick_post= input("Which post would you like to read from the list? ")
            if pick_post == "None":
                print("No tasks were read. ")
                break
            try:
                pick_post = int(pick_post) - 1
                if 0 <= pick_post < len(dir_list):
                    posts_folder_name = "blog_posts"
                    script_dir = os.path.dirname(__file__)
                    posts_dir = os.path.join(script_dir, posts_folder_name)
                    filename = dir_list[pick_post]
                    full_path = os.path.join(posts_dir, filename)
                    print("\n")
                    with open(full_path, 'r') as file:
                        file_content = file.read()

                    print(file_content)
                    print("\n")

                    print(f"You have successfully read '{dir_list[pick_post]}' from the list. ")
                    break
                    print("\n")   
                else:
                    print(f"The list is only {len(dir_list)} task(s) long, not {pick_post + 1}. ")
            except ValueError:
                print("That is not a number. Try again")

    elif command == "delete" or command == "d":
        posts_folder_name = "blog_posts"
        script_dir = os.path.dirname(__file__)
        posts_dir = os.path.join(script_dir, posts_folder_name)
        # dir_list = os.listdir(posts_folder_name)
        # print(dir_list)
        try:
            dir_list = os.listdir(posts_dir)
            if not dir_list:
                print("No blog posts found.")
            else:
                print("\n--- Your Blog Posts ---")
            for index, filename in enumerate(dir_list, start=1):
                print(f"{index}. {filename}")
            print("\n")
        except FileNotFoundError:
            print("The blog_posts directory does not seem to exist yet. Create a post first.")
        
        while True:
            remove_item = input("Which file would you like to remove? ")
            if remove_item == "None":
                print("No files were removed. ")
                break
            try:
                remove_item = int(remove_item) - 1
                if 0 <= remove_item < len(dir_list):
                    posts_folder_name = "blog_posts"
                    script_dir = os.path.dirname(__file__)
                    posts_dir = os.path.join(script_dir, posts_folder_name)
                    filename = dir_list[remove_item]
                    full_path = os.path.join(posts_dir, filename)

                    print("\n")
                    print("--- Your File ---")
                    with open(full_path, 'r') as file:
                        file_content = file.read()

                    print(file_content)
                    print("\n")

                    while True:
                        confirmation = input("Are you sure you want to delete the above file? ")
                        if confirmation.lower() == "n" or confirmation.lower() == "no":
                            print("No files were removed. ")
                            break
                        elif confirmation == "y" or confirmation.lower() == "yes":
                            os.remove(full_path)
                            print(f"You have successfully removed '{dir_list[remove_item]}' from the files. ")
                            break
                        else:
                            print("Answer 'y/n'. Try again")
                        
                    print("\n")
                    break
                else:
                    print(f"The list is only {len(dir_list)} task(s) long, not {remove_item + 1}. ")

            except ValueError:
                print("That is not a number. Try again")

    elif command == "quit" or command == "q":
        break

    else:
        print("You can either CREATE(c), READ(r), LIST(l), DELETE(d) files or QUIT(q). Try Again")

