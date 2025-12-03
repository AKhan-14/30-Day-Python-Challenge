# The Challenge: Use a lightweight web framework to turn your Day 15 Contact Book into a REST API. 
# Create endpoints to get all contacts, get a specific contact by name, 
# and add a new contact using a tool like Postman or curl.

# Step 0: Setup - Installing Flask
# pip install flask

# Step 1: The "Hello, World" Web Server

"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloworld():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()
"""

# Step 2: Rebuilding the In-Memory Database

"""
from flask import Flask

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

app = Flask(__name__)
contact_book = ContactBook()
contact_book.add_contact("Ada Lovelace", "123-456-7890", "ada@example.com")
contact_book.add_contact("John Bobby", "676-767-6767", "jb67@example.com")

@app.route('/')
def helloworld():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()
"""

# Step 3: CREATE Endpoint #1: Get All Contacts (GET /contacts)

"""
from flask import Flask , jsonify

class Contact:
    def __init__(self,name,phone_number,email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Email {self.email}"
    
    def to_dict(self):
        return {'Name': self.name, 'Phone': self.phone_number, 'Email': self.email}
    
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

app = Flask(__name__)
contact_book = ContactBook()
contact_book.add_contact("Ada Lovelace", "123-456-7890", "ada@example.com")
contact_book.add_contact("John Bobby", "676-767-6767", "jb67@example.com")

@app.route('/')
def helloworld():
    return "Hello, World!"

@app.route('/contacts')
def get_all_contacts():
    all_contacts = contact_book.contacts.values()

    contacts_as_dicts = []
    for contact in all_contacts:
        contacts_as_dicts.append(contact.to_dict())

    return jsonify(contacts_as_dicts)

if __name__ == "__main__":
    app.run()
"""

# Step 4: CREATE Endpoint #2: Get a Specific Contact (GET /contacts/<name>)

"""
from flask import Flask , jsonify

class Contact:
    def __init__(self,name,phone_number,email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Email {self.email}"
    
    def to_dict(self):
        return {'Name': self.name, 'Phone': self.phone_number, 'Email': self.email}
    
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

app = Flask(__name__)
contact_book = ContactBook()
contact_book.add_contact("Ada Lovelace", "123-456-7890", "ada@example.com")
contact_book.add_contact("John Bobby", "676-767-6767", "jb67@example.com")

@app.route('/')
def helloworld():
    return "Hello, World!"

@app.route('/contacts')
def get_all_contacts():
    all_contacts = contact_book.contacts.values()

    contacts_as_dicts = []
    for contact in all_contacts:
        contacts_as_dicts.append(contact.to_dict())

    return jsonify(contacts_as_dicts)

@app.route('/contacts/<name>')
def get_contact(name):
    found_contact = contact_book.find_contact(name)

    if found_contact:
        return jsonify(found_contact.to_dict())
    else:
        error_message = {"error": "Contact not found"}

        return jsonify(error_message), 404

if __name__ == "__main__":
    app.run()
"""

# Step 5: CREATE Endpoint #3: Add a New Contact (POST /contacts)

from flask import Flask , jsonify , request

class Contact:
    def __init__(self,name,phone_number,email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Email {self.email}"
    
    def to_dict(self):
        return {'Name': self.name, 'Phone': self.phone_number, 'Email': self.email}
    
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

app = Flask(__name__)
contact_book = ContactBook()
contact_book.add_contact("Ada Lovelace", "123-456-7890", "ada@example.com")
contact_book.add_contact("John Bobby", "676-767-6767", "jb67@example.com")

@app.route('/')
def helloworld():
    return "Hello, World!"

@app.route('/contacts', methods=["GET"])
def get_all_contacts():
    all_contacts = contact_book.contacts.values()

    contacts_as_dicts = []
    for contact in all_contacts:
        contacts_as_dicts.append(contact.to_dict())

    return jsonify(contacts_as_dicts)

@app.route('/contacts/<name>', methods=["GET"])
def get_contact(name):
    found_contact = contact_book.find_contact(name)

    if found_contact:
        return jsonify(found_contact.to_dict())
    else:
        error_message = {"error": "Contact not found"}

        return jsonify(error_message), 404

@app.route('/contacts', methods=["POST"])
def add_contact():
    incoming_data = request.get_json() 

    name = incoming_data.get('name')
    phone = incoming_data.get('phone')
    email = incoming_data.get('email')

    contact_book.add_contact(name, phone, email)

    success_message = {'message': 'Contact created successfully!'}

    return jsonify(success_message), 201

if __name__ == "__main__":
    app.run()