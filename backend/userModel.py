## userModel.py
from pymongo import MongoClient
from werkzeug.security import generate_password_hash
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGO_URI)
db = client["UserDB"]
user_collection = db["users"]

# User Schema
def create_user(email, password):
    hashed_password = generate_password_hash(password)
    user = {
        "email": email,
        "password": hashed_password
    }
    user_collection.insert_one(user)


def find_user_by_email(email):
    return user_collection.find_one({"email": email})

