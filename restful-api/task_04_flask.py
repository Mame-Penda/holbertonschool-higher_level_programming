#!/usr/bin/python3
"""Develop a Simple API using Python with Flask."""
from flask import Flask, request, jsonify


app = Flask(__name__)
"""recurement"""


users = {}


@app.route('/')
def home():
    """Return str"""
    return "Welcome to the Flask API!"


@app.route('/data')
def list_users():
    """Return list of users in data path"""
    return jsonify(list(users.keys()))


@app.route('/status')
def send_status():
    """Return str in status path"""
    return "ok"


@app.route('/users/<username>')
def get_user(username):
    """Return a user data"""
    user = users.get(username)
    if user:
        return jsonify(users)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Return user in users."""
    user_data = request.get_json()
    if not user_data or "username" not in user_datadata:
        return jsonify({"error": "USername is required"}), 400

    username = user_data["username"]
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201


if __name__ == "__main__":
    app.run(debug=True)
