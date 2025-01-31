
## server.py
from flask import Flask
from userRoute import user_bp
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Register blueprints
app.register_blueprint(user_bp, url_prefix='/api/users')

if __name__ == "__main__":
    app.run(port=4000, debug=True)
