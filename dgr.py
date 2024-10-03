import os
from dotenv import load_dotenv
from flask import Flask

# Load environment variables from .env file
load_dotenv()

# Get the environment variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
CODESPACE_NAME = os.getenv('CODESPACE_NAME')
OWNER_NAME = os.getenv('OWNER_NAME')
REPO_NAME = os.getenv('REPO_NAME')
PORT = os.getenv('PORT', 5000)  # Use the PORT environment variable

app = Flask(__name__)

@app.route('/')
def index():
    return f"Running in Codespace: {CODESPACE_NAME}, Owner: {OWNER_NAME}, Repository: {REPO_NAME}"

if __name__ == "__main__":
    # Start the Flask app
    app.run(host='0.0.0.0', port=int(PORT))
