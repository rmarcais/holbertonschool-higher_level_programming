#!/usr/bin/python3
"""API Security and Authentication Techniques"""

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity, JWTManager

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "holberton-secret-key"
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("hello"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("test"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username).get("password"), password):
        return username


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted", 200


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    if username not in users or not check_password_hash(users.get(username).get("password"), password):
        return jsonify({"error": "Bad credentials"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted", 200


@app.route("/admin-only")
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if users.get(current_user).get("role") == "admin":
        return "Admin Access: Granted", 200
    return "Admin Access Forbidden", 403


# Custom Error Handlers
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err, payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err, payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err, payload):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
