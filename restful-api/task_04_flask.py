#!/usr/bin/python3
"""Develop a Simple API using Python with Flask."""
from flask import Flask, request, jsonify


app = Flask(__name__)
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
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Return user in users."""
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error": "USername is required"}), 400
    users[data["Username"]] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
