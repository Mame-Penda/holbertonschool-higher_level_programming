#!/usr/bin/python3
"""
Un script Python basique pour récupérer des posts de
JSONPlaceholder en utilisant requests
"""
from flask import Flask, jsonify, request
"""importation"""


app = Flask(__name__)
"""recurement"""


users = {}


@app.route("/")
def home():
    """home"""
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """Return a list of all usernames in the 'users' dictionary"""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """status"""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Check if the user exists in the dictionary"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Parse the incoming JSON data"""
    user_data = request.get_json()
    if not user_data or "username" not in user_data:
        return jsonify({"error": "Username is required"}), 400

    username = user_data["username"]
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201


if __name__ == "__main__":
    app.run(debug=True)
