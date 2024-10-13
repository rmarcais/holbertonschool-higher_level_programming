#!/usr/bin/python3
"""Simple API using Python with Flask"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Some data to test functions
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!", 200


@app.route("/data")
def data():
    return jsonify([username for username in users]), 200


@app.route("/status")
def status():
    return "OK", 200


@app.route("/users/<username>")
def user_data(username):
    status = 200
    data = users.get(username)
    if not data:
        data = {"error": "User not found"}
        status = 404

    return jsonify(data), status


@app.route("/add_user", methods=["POST"])
def add_user():
    status = 201
    parsed_json = request.get_json()
    username = parsed_json.get("username")
    message = parsed_json

    if username:
        users[username] = parsed_json
    else:
        status = 400
        message = {"error": "Username is required"}

    return jsonify(message), status


if __name__ == "__main__":
    app.run()
