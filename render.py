import os
import time
from dotenv import load_dotenv
from flask import Flask

# Load environment variables from .env file
load_dotenv()

# Get the environment variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
CODESPACE_NAME = os.getenv('CODESPACE_NAME')
OWNER_NAME = os.getenv('OWNER_NAME')
REPO_NAME = os.getenv('REPO_NAME')
PORT = os.getenv('PORT', 5000)  # Default to 5000 if PORT is not set

app = Flask(__name__)

@app.route('/')
def index():
    return f"Running in Codespace: {CODESPACE_NAME}, Owner: {OWNER_NAME}, Repository: {REPO_NAME}"

def main():
    print(f"Starting application on port {PORT}...")
    app.run(host='0.0.0.0', port=int(PORT))  # Run the Flask app

if __name__ == "__main__":
    main()
