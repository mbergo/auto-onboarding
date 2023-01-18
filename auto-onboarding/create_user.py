import argparse
import json
import requests

# parse the command line arguments
parser = argparse.ArgumentParser(description='Create Office365 user')
parser.add_argument('name', help='Name of the user')
parser.add_argument('email', help='Email of the user')
parser.add_argument('password', help='Password of the user')
args = parser.parse_args()

# Load the token from the token.json file
with open('token.json', 'r') as f:
    token = json.load(f)['access_token']

# Define the endpoint for creating a user in Office 365
url = 'https://graph.microsoft.com/v1.0/users'

# Define the data for the new user
data = {
    'accountEnabled': True,
    'displayName': args.name,
    'mailNickname': args.email.split('@')[0],
    'userPrincipalName': args.email,
    'passwordProfile': {
        'forceChangePasswordNextSignIn': True,
        'password': args.password
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
