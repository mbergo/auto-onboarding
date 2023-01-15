#!/usr/bin/env python3

import json
import requests
import sys

# Get command line arguments
name = sys.argv[1]
email = sys.argv[2]
password = sys.argv[3]

# Replace with your own access token"
with open('token.json') as f:
    data = json.load(f)
    access_token = data['access_token']
# Build the request body
data = {
    "accountEnabled": True,
    "displayName": name,
    "mailNickname": name,
    "userPrincipalName": email,
    "passwordProfile": {
        "forceChangePasswordNextSignIn": True,
        "password": password
    }
}

# Make the request to create the user
url = "https://graph.microsoft.com/v1.0/users"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}
response = requests.post(url, headers=headers, json=data)

# Check for success
if response.status_code == 201:
    print("Successfully created user.")
else:
    print("Failed to create user.")
    print(response.text)
