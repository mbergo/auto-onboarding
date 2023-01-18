import argparse
import json
import requests

# parse the command line arguments
name = argv[1]
email = argv[2]
password = argv[3]

# Load the token from the token.json file
with open('token.json', 'r') as f:
    token = json.load(f)['access_token']

# Define the endpoint for creating a user in Office 365
url = 'https://graph.microsoft.com/v1.0/users'

# Define the data for the new user
data = {
    'accountEnabled': True,
    'displayName': name,
    'mailNickname': email.split('@')[0],
    'userPrincipalName': email,
    'passwordProfile': {
        'forceChangePasswordNextSignIn': True,
        'password': password
    }
}

# Set the headers for the request
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

# Make the request to create the user
response = requests.post(url, json=data, headers=headers)

# Check the status code of the response
if response.status_code != 201:
    print('Error creating user:', response.text)
else:
    print('User created successfully!')
