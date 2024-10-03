import os
import requests
import time
import logging
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Display your message at the top
print("THIS SCRIPT MADE BY :- @TitanDevop")
print("OFFICIAL TG :- @Titanddosop")
print("------------------------------------------------------")

# Set up logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

# Expiry system: set the expiry date (YYYY-MM-DD)
EXPIRY_DATE = "2024-10-10"

# Function to check if the script is expired
def check_expiry():
    current_date = datetime.now().date()
    expiry_date = datetime.strptime(EXPIRY_DATE, "%Y-%m-%d").date()

    if current_date > expiry_date:
        print("Script has expired .... Get New By @TitanDevop")
        exit(1)  # Exit if the script is expired

# Function to get the GitHub token from the environment variable
def get_github_token():
    token = os.getenv('GITHUB_TOKEN')  # Read token from .env file
    if token is None:
        logging.error("GITHUB_TOKEN not found in .env file.")
        exit(1)
    return token

# Function to get the Codespace name automatically
def get_codespace_name(token):
    headers = {"Authorization": f"token {token}"}
    try:
        response = requests.get("https://api.github.com/user/codespaces", headers=headers)
        response.raise_for_status()
        codespaces = response.json().get('codespaces', [])

        if codespaces and isinstance(codespaces, list) and len(codespaces) > 0:
            return codespaces[0]["name"]  # Assuming you want the first Codespace
        else:
            logging.error("No Codespaces found for the user.")
            exit(1)
    except requests.RequestException as e:
        logging.error(f"Error fetching Codespace name: {e}")
        exit(1)

def start_codespace(token, codespace_name):
    logging.info(f"Starting Codespace: {codespace_name}")
    headers = {"Authorization": f"token {token}"}
    try:
        response = requests.post(f"https://api.github.com/user/codespaces/{codespace_name}/start", headers=headers)
        response.raise_for_status()
        logging.info(f"Codespace {codespace_name} is starting.")
    except requests.RequestException as e:
        logging.error(f"Error starting Codespace: {e}")

def keep_alive(token, codespace_name):
    headers = {"Authorization": f"token {token}"}
    last_status = None  # Store the last status to reduce unnecessary logs
    while True:
        try:
            response = requests.get(f"https://api.github.com/user/codespaces/{codespace_name}", headers=headers)
            response.raise_for_status()
            status = response.json().get("state", "Unknown")

            if status != last_status:
                logging.info(f"Codespace state changed: {status}")
                last_status = status

            if status == "Shutdown":
                logging.info(f"Codespace {codespace_name} is shut down. Attempting to restart...")
                start_codespace(token, codespace_name)
            else:
                logging.debug(f"Codespace {codespace_name} is running.")  # Lower log level to debug for normal state

            time.sleep(60)  # Ping the Codespace API every minute
        except requests.RequestException as e:
            logging.error(f"Error pinging Codespace API: {e}")
            time.sleep(60)

if __name__ == "__main__":
    check_expiry()  # Check if the script has expired
    github_token = get_github_token()  # Read token from .env
    codespace_name = get_codespace_name(github_token)  # Get the Codespace name
    keep_alive(github_token, codespace_name)  # Keep the Codespace alive
