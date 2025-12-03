# The Challenge: Create a command-line password manager. 
# A user should have a master password to unlock it. 
# It should be able to store and retrieve passwords for different services. 
# Warning: Do not use this for real passwords!

# Step 0: Setup - Installing the Cryptography Library
# pip install bcrypt
"""
import bcrypt

"""
# Step 1: The PasswordManager Class

"""
class PasswordManager:
    def __init__(self,data_file,master_key_file):
        self.data_file = data_file
        self.master_key_file = master_key_file
        self.passwords = {}
"""

# Step 2: The First Run - Setting the Master Password

"""
import bcrypt
import os

class PasswordManager:
    def __init__(self,data_file,master_key_file):
        self.data_file = data_file
        self.master_key_file = master_key_file
        self.passwords = {}
        self.master_key_hash = None

    def setup_master_password(self):
        if not os.path.exists(self.master_key_file):
            master_password = input("Create a new master password: ")

            # converting password to array of bytes
            bytes = master_password.encode('utf-8')

            # generating the salt
            salt = bcrypt.gensalt()

            # Hashing the password
            self.master_key_hash = bcrypt.hashpw(bytes, salt)

            with open(self.master_key_file, 'wb') as file:
                file.write(self.master_key_hash)
            print("Master password created and saved securely.")

        else:
            with open(self.master_key_file, "rb") as file:
                self.master_key_hash = file.read()
"""

# Step 3: Unlocking the Vault - Verifying the Master Password

"""
import bcrypt
import os

class PasswordManager:
    def __init__(self,data_file,master_key_file):
        self.data_file = data_file
        self.master_key_file = master_key_file
        self.passwords = {}
        self.master_key_hash = None

    def setup_master_password(self):
        if not os.path.exists(self.master_key_file):
            master_password = input("Create a new master password: ")

            # converting password to array of bytes
            bytes = master_password.encode('utf-8')

            # generating the salt
            salt = bcrypt.gensalt()

            # Hashing the password
            self.master_key_hash = bcrypt.hashpw(bytes, salt)

            with open(self.master_key_file, 'wb') as file:
                file.write(self.master_key_hash)
            print("Master password created and saved securely.")

        else:
            with open(self.master_key_file, "rb") as file:
                self.master_key_hash = file.read()

    def verify_master_password(self):
        prompt_password = input("Enter your master password: ")
        prompt_password_bytes = prompt_password.encode('utf-8')
        if bcrypt.checkpw(prompt_password_bytes, self.master_key_hash):
            print("Password verified successfully.")
            return True
        else:
            print("Invalid password. Exiting.")
            return False
"""

# Step 4: The Main Application Logic (CRUD)

import bcrypt
import os
import json

class PasswordManager:
    def __init__(self,data_file,master_key_file):
        self.data_file = data_file
        self.master_key_file = master_key_file
        self.passwords = self.load_passwords()
        self.master_key_hash = None

    def setup_master_password(self):
        if not os.path.exists(self.master_key_file):
            master_password = input("\nCreate a new master password: ")

            # converting password to array of bytes
            bytes = master_password.encode('utf-8')

            # generating the salt
            salt = bcrypt.gensalt()

            # Hashing the password
            self.master_key_hash = bcrypt.hashpw(bytes, salt)

            with open(self.master_key_file, 'wb') as file:
                file.write(self.master_key_hash)
            print("\nMaster password created and saved securely.")

        else:
            with open(self.master_key_file, "rb") as file:
                self.master_key_hash = file.read()

    def verify_master_password(self):
        prompt_password = input("\nEnter your master password: ")
        prompt_password_bytes = prompt_password.encode('utf-8')
        if bcrypt.checkpw(prompt_password_bytes, self.master_key_hash):
            print("\nPassword verified successfully.")
            return True
        else:
            print("\nInvalid password. Exiting.")
            return False

    def save_passwords(self): 
        with open(self.data_file, 'w') as file:
            json.dump(self.passwords, file)

    def load_passwords(self): 
        try:
            with open('passwords.json', 'r') as file: 
                return json.load(file) 
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}
    
    def add_password(self):
        new_title = input("\nWhat is the name of your service? ")
        print("Service created successfully!")
        new_password = input("\nWhat is the password for your service? ")
        print("Password created successfully!")
        self.passwords[new_title] = new_password
        # print(password_dict)
        self.save_passwords()
        print(f"Password for {new_title} added and saved successfully!")

    def get_password(self):
        target = input("\nWhich password are you looking for? ")
        if target in self.passwords:
            print(f"Password for {target} is {self.passwords.get(target)}!")

    def list_password(self):
        if self.passwords == {}:
            print("The service list is empty!")
        else:
            print("\nYour Service List:")
            for index, key in enumerate(self.passwords, start=1):
                print(f"{index}. {key}")
    
    def delete_password(self):
        target = input("\nWhich password do you want to delete? ")
        if target in self.passwords:
            del self.passwords[target]
            self.save_passwords()
            print(f"Password for {target} was deleted!")
        else:
            print(f"\nThere is no service named {target}! Check the list of current services using list")


# --- Main Application ---

# 1. Create an instance of the manager
manager = PasswordManager(data_file="passwords.json", master_key_file="master_key.key")

# 2. Run the one-time setup or load the existing key
manager.setup_master_password()

# 3. Verify the user has access.
#    The 'if' statement is the gatekeeper to the rest of the app.
if manager.verify_master_password():
    
    # 4. If verification is successful, start the main command loop
    while True:
        command = input("\nWhat would you like to do? ADD(a), GET(g), LIST(l), DELETE(d) files or QUIT(q)? ").strip().lower()

        if command == "add" or command == "a":
            manager.add_password() 
        
        elif command == "get" or command == "g":
            manager.get_password()
            
        elif command == "list" or command == "l":
            manager.list_password()
            
        elif command == "delete" or command == "d":
            manager.delete_password()
            
        elif command == "quit" or command == "q":
            print("Exiting.")
            break
        else:
            print("You can either ADD(a), GET(g), LIST(l), DELETE(d) files or QUIT(q). Try Again")
