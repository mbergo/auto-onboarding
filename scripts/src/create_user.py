import json
import argparse
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Put your client secrets in a json file
CLIENT_SECRET_FILE = 'client_secret.json'
creds = Credentials.from_authorized_user_info(info=json.loads(CLIENT_SECRET_FILE), scopes=['https://www.googleapis.com/auth/admin.directory.user'])

# Build the API client
directory_service = build('admin', 'directory_v1', credentials=creds)

# Define the new user's details
def create_user(name, email, password):
    new_user = {
        'primaryEmail': email,
        'name': {
            'givenName': name.split()[0],
            'familyName': name.split()[1]
        },
        'password': password
    }

    # Create the user
    try:
        directory_service.users().insert(body=new_user).execute()
        print(f'User {new_user["primaryEmail"]} created successfully.')
    except HttpError as error:
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a new user with email on the predify.me')
    parser.add_argument('name', type=str, help='Full name of the user')
    parser.add_argument('email', type=str, help='Email of the user')
    parser.add_argument('password', type=str, help='Password of the user')
    args = parser.parse_args()
    create_user(args.name, args.email, args.password)
