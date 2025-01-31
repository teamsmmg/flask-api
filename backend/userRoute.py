## userRoute.py
from flask import Blueprint
from userController import UserController

user_bp = Blueprint('users', __name__)

# Define routes
user_bp.route('/signup', methods=['POST'])(UserController.signup)
user_bp.route('/login', methods=['POST'])(UserController.login)

