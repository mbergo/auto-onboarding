import requests
import json
import argparse

# Put your access token in a json file
ACCESS_TOKEN_FILE = 'access_token.json'
access_token = json.loads(open(ACCESS_TOKEN_FILE).read())['access_token']

# Define the new user's details
def create_user(name, email, password):
    # Create the user
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }

    data = {
        "accountEnabled": True,
        "displayName": name,
        "mailNickname": name.split()[0],
        "userPrincipalName": email,
        "passwordProfile" : {
        "password" : password,
        "forceChangePasswordNextSignIn": True
        }
    }

    url = 'https://graph.microsoft.com/v1.0/users'
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        print(f'User {email} created successfully')
    except requests.exceptions.HTTPError as error:
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a new user with email on the predify.me')
    parser.add_argument('name', type=str, help='Full name of the user')
    parser.add_argument('email', type=str, help='Email of the user')
    parser.add_argument('password', type=str, help='Password of the user')
    args = parser.parse_args()
    create_user(args.name, args.email, args.password)
