# The Challenge: Take your Day 6 Contact Book and rewrite it using classes. 
# Create a Contact class and a ContactBook class.

# Day 6 Contact Book
"""
contact_book = {
    "Gary Nike" : {
        "phone_number" : "63",
        "email" : "garynike63@email.com"
    },
    "Cristiano Ronaldo" : {
        "phone_number" : "7",
        "email" : "CR7@email.com"
    },
    "Thomas Shelby" : {
        "phone_number" : "1",
        "email" : "PeakyBlinder1@email.com"
    }
}

while True:
    command = input("What would you like to do? ").strip().lower()
    if command == "quit" or command == "q":
        break
    elif command == "add" or command == "a":
        while True:
            new_contact_name = input("1: What is the new contact's name? ")
            if new_contact_name in contact_book:
                print("This name already exists in your contacts. Please use a different name.")
                continue
            if not new_contact_name.strip():
                print("Name cannot be empty. Please try again.")
                continue
            break
        print(f"The new contact's name is {new_contact_name}.")

        new_contact_number = input("2: What is the new contact's number? ")
        print(f"The new contact's number is {new_contact_number}.")

        while True:
            new_contact_email = input("3: What is the new contact's email? ")
            if new_contact_email.count("@email.com") == 1:
                print(f"The new contact's email is {new_contact_email}.")
                break
            else:
                print("The email must be in the form 'example@email.com', Try Again")

        contact_book[new_contact_name] = {"phone_number": new_contact_number, "email": new_contact_email}
        #contact_book.update({f"{new_contact_name}" : {"phone_number" : f"{new_contact_number}","email" : f"{new_contact_email}"}})
        print("New contact added successfully! ")
        print(contact_book)
    elif command == "lookup" or command == "l":
        while True:
            contact_lookup = input("Which name are you looking for? ")
            if contact_lookup in contact_book:
                print("Contact found successfully!")
                print(f"{contact_lookup}'s number is: {contact_book[contact_lookup]["phone_number"]}")
                print(f"{contact_lookup}'s email is: {contact_book[contact_lookup]["email"]}")
                break
            else:
                print("This contact does not exist in your contact book.")
    else:
        print("That is NOT a valid command, try again. ")
        continue
"""

# Step 1: The Blueprint for a Person - The Contact Class
# Represents a single contact

"""
class Contact:
    def __init__(self,name,phone_number,email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Email {self.email}"
"""
    
# Step 2: The Manager - The ContactBook Class

"""
class Contact:
    def __init__(self,name,phone_number,email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Email {self.email}"
    
class ContactBook:
    def __init__(self):
        self.contacts = {}
"""

# Step 3: Implementing the ContactBook Methods

"""
class Contact:
    def __init__(self,name,phone_number,email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Email {self.email}"
    
class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self,name,phone_number,email):
        new_contact = Contact(name,phone_number,email)
        self.contacts[name] = new_contact
    
    def find_contact(self,name):
        if name in self.contacts:
            return self.contacts[name]
        else:
            return None
    
#    def display_contacts(self):
#        if not self.contacts:
#            print("The contact book is empty")
#            return
#        else:
#            print("--- Your Contacts ---")
#            for contact in self.contacts:
#                print(contact)
#            print("---------------------")
"""

# Step 4: Rewriting the Main Application Logic

class Contact:
    def __init__(self,name,phone_number,email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Email {self.email}"
    
class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self,name,phone_number,email):
        new_contact = Contact(name,phone_number,email)
        self.contacts[name] = new_contact
    
    def find_contact(self,name):
        if name in self.contacts:
            return self.contacts[name]
        else:
            return None

my_book = ContactBook()
while True:
    command = input("What would you like to do? ").strip().lower()
    if command == "quit" or command == "q":
        break
    elif command == "add" or command == "a":
        while True:
            new_contact_name = input("1: What is the new contact's name? ")
            if my_book.find_contact(new_contact_name) is not None:
                print("This name already exists in your contacts. Please use a different name.")
                continue
            if not new_contact_name.strip():
                print("Name cannot be empty. Please try again.")
                continue
            break
        print(f"The new contact's name is {new_contact_name}.")

        new_contact_number = input("2: What is the new contact's number? ")
        print(f"The new contact's number is {new_contact_number}.")

        while True:
            new_contact_email = input("3: What is the new contact's email? ")
            if new_contact_email.count("@email.com") == 1:
                print(f"The new contact's email is {new_contact_email}.")
                break
            else:
                print("The email must be in the form 'example@email.com', Try Again")

        my_book.add_contact(new_contact_name,new_contact_number,new_contact_email)
        #contact_book[new_contact_name] = {"phone_number": new_contact_number, "email": new_contact_email}
        #contact_book.update({f"{new_contact_name}" : {"phone_number" : f"{new_contact_number}","email" : f"{new_contact_email}"}})
        print("New contact added successfully! ")

    elif command == "lookup" or command == "l":
        while True:
            contact_lookup = input("Which name are you looking for? ")
            found_contact = my_book.find_contact(contact_lookup)
            if found_contact:
                print("Contact found successfully!")
                print(found_contact)
                break
            else:
                print("This contact does not exist in your contact book.")
    else:
        print("That is NOT a valid command, try again. ")
        continue