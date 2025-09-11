# The Challenge: Create an in-memory contact book. 
# You should be able to add a new contact with a name, phone number, and email. 
# You should also be able to look up a contact by name.

# Step 1: The Most Important Step - Data Modeling

"""

# contact_book = {"name" : "Conor Mcgregor", "phone_number" : "2", "email" : "doublechamp@email.com"}

contact_book = {
    "Gary Nike" : {
        "phone_number" : "63",
        "email" : "garynike63@email.com"
    },
    "Cristiano Ronaldo" : {
        "phone_number" : "7",
        "email" : "CR7@email.com"
    },
    "Andrew Tate" : {
        "phone_number" : "888",
        "email" : "TopG@email.com"
    }
    "Nate Diaz" : {
        "phone_number" : "209"
        "email" : "NateDiaz209@email.com"
    }
    }

print(contact_book.items())

"""

# Step 2-4: The Application Skeleton

contact_book = {
    "Gary Nike" : {
        "phone_number" : "63",
        "email" : "garynike63@email.com"
    },
    "Cristiano Ronaldo" : {
        "phone_number" : "7",
        "email" : "CR7@email.com"
    },
    "Andrew Tate" : {
        "phone_number" : "888",
        "email" : "TopG@email.com"
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