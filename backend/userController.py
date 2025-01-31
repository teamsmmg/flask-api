## userController.py
from flask import request, jsonify
from userModel import create_user, find_user_by_email
from werkzeug.security import check_password_hash

# User Controller
class UserController:
    @staticmethod
    def signup():
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({"message": "Email and password are required"}), 400

        if find_user_by_email(email):
            return jsonify({"message": "User already exists"}), 409

        create_user(email, password)
        return jsonify({"message": "User registered successfully"}), 201

    @staticmethod
    def login():
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        user = find_user_by_email(email)
        if not user or not check_password_hash(user["password"], password):
            return jsonify({"message": "Invalid email or password"}), 401

        return jsonify({"message": "Login successful"}), 200

