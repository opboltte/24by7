import os
import time
import requests
from dotenv import load_dotenv
from flask import Flask
from threading import Thread

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

def ping_codespace():
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    while True:
        try:
            # Ping the Codespace API
            response = requests.get(f"https://api.github.com/user/codespaces/{CODESPACE_NAME}", headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            status = response.json().get("state", "Unknown")
            print(f"Codespace status: {status}")
        except requests.RequestException as e:
            print(f"Error pinging Codespace: {e}")

        # Wait for 60 seconds before the next ping
        time.sleep(60)

if __name__ == "__main__":
    # Start the pinging thread
    ping_thread = Thread(target=ping_codespace)
    ping_thread.daemon = True  # Allow thread to exit when the main program exits
    ping_thread.start()

    # Start the Flask app
    app.run(host='0.0.0.0', port=int(PORT))
