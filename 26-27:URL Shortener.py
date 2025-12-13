# The Challenge: This is a classic system design question. 
# Build a service with two main parts:
# An API endpoint that takes a long URL and returns a short URL (e.g., localhost:5000/a3x7b).
# A mechanism where visiting the short URL redirects the user to the original long URL.

# Part 1: The Core Logic & Data Model

# Step 1: The "Database" - Storing the Mappings
"""
database = {}
"""

# Step 2: The "Engine" - Generating a Unique Short Code
"""
import random
from flask import Flask , request
database = {}

def generatecode():
    safe_characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    length = 6

    while True:
        code = ''.join(random.choice(safe_characters) for i in range(length))
        if code not in database:
            return code
"""
# Part 2: The Back-End API (using Flask)

# Step 3: The Setup
import random
from flask import Flask , jsonify , request , redirect

app = Flask(__name__)

database = {}

def generatecode():
    safe_characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    length = 6

    while True:
        code = ''.join(random.choice(safe_characters) for i in range(length))
        if code not in database:
            return code
    
# Step 4: The "Create" Endpoint (POST /shorten)
@app.route("/shorten", methods = ["POST"])
def create_short_url():
    incoming_data = request.get_json() 
    if not incoming_data:
        return jsonify({"error": "No data provided"}), 400

    long_url = incoming_data.get('url')
    if not long_url or not long_url.startswith(('http://', 'https://')):
        return jsonify({"error": "Invalid or missing URL"}), 400
    
    short_code = generatecode()
    database[short_code] = long_url

    short_url = request.host_url + short_code

    return jsonify({
        "message": "URL shortened successfully!",
        "short_url": short_url,
        "long_url": long_url
    }), 201

# Step 5: The "Redirect" Endpoint (GET /<short_code>)
@app.route("/<short_code>", methods = ["GET"])
def redirect_to_url(short_code):
    if short_code in database:
        long_url = database[short_code]
        return redirect(long_url, code=301)
    else:
        return jsonify({"error": "Short URL not found"}), 404

if __name__ == '__main__':
    app.run()