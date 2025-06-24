# Coding With Kien - 365 Days of Python Programming
# Advanced - Day 05

# Simple API server with Flask
# You may need to install Flask first:
# pip install Flask

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/api/data")
def get_data():
    data = {"name": "Kien", "age": 20}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

# To run this, save it as a Python file (e.g., api.py) and run `python api.py`
# Then, open your browser and go to http://127.0.0.1:5000/ to see the greeting,
# or http://127.0.0.1:5000/api/data to see the JSON data. 