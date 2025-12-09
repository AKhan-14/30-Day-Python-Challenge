# The Challenge: Create a simple web-based front-end for your To-Do list. 
# It should have a text box to add a task and a button. 
# When you add a task, it should call the REST API you built (or a new one) to save the task, 
# and then update the list shown on the page.

# Part 1: The Back-End - A Simple To-Do API (using Flask)
# Step 1: The Basic Setup

"""
from flask import Flask , jsonify

database = ["Train hard", "Eat whole natural foods", "Make money"]
"""

# Step 2: The "Read" Endpoint (GET /tasks)

"""
from flask import Flask , jsonify , request

database = ["Train hard", "Eat whole natural foods", "Make money"]

app = Flask(__name__)

@app.route("/tasks", methods = ["GET"])
def get_tasks():
    return jsonify(database)
"""

# Step 3: The "Create" Endpoint (POST /tasks)

from flask import Flask , jsonify , request , render_template

database = ["Train hard", "Eat whole natural foods", "Make money"]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/tasks", methods = ["GET"])
def get_tasks():
    return jsonify(database)

@app.route("/tasks", methods = ["POST"])
def add_task():
    incoming_data = request.get_json() 

    task = incoming_data.get('task')
    database.append(task)

    success_message = {'message': 'Task added successfully!'}

    return jsonify(success_message), 201

if __name__ == "__main__":
    app.run()