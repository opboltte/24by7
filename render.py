import os
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the environment variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
CODESPACE_NAME = os.getenv('CODESPACE_NAME')
OWNER_NAME = os.getenv('OWNER_NAME')
REPO_NAME = os.getenv('REPO_NAME')

def main():
    # Example of what you might want to do with these variables
    print(f"Running in Codespace: {CODESPACE_NAME}")
    print(f"Owner: {OWNER_NAME}, Repository: {REPO_NAME}")

    # Here you can add your main logic
    while True:
        # This is where you would implement your functionality
        print("Performing task...")
        # Sleep for a certain period (e.g., every 60 seconds)
        time.sleep(30)

if __name__ == "__main__":
    main()
