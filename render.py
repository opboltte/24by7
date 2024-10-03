import os
import time
import socket
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the environment variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
CODESPACE_NAME = os.getenv('CODESPACE_NAME')
OWNER_NAME = os.getenv('OWNER_NAME')
REPO_NAME = os.getenv('REPO_NAME')

def scan_ports(target_ip, port_range):
    open_ports = []
    for port in port_range:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Set a timeout for the connection attempt
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                open_ports.append(port)

    return open_ports

def main():
    # Example of what you might want to do with these variables
    print(f"Running in Codespace: {CODESPACE_NAME}")
    print(f"Owner: {OWNER_NAME}, Repository: {REPO_NAME}")

    # Define the target IP and port range for scanning
    target_ip = "192.168.1.1"  # Replace with the actual target IP address
    port_range = range(1, 1025)  # Scanning ports 1 to 1024

    while True:
        print("Performing task...")

        # Call the port scanning function
        open_ports = scan_ports(target_ip, port_range)

        if open_ports:
            print(f"Open ports detected: {open_ports}")
        else:
            print("No open ports detected, continuing to scan...")

        # Sleep for a certain period (e.g., every 60 seconds)
        time.sleep(60)

if __name__ == "__main__":
    main()
