#!/bin/bash

# Update the system
sudo apt-get update

# Install Nginx
sudo apt-get install -y nginx

# Install pip and virtualenv
sudo apt-get install -y python3-pip
sudo pip3 install virtualenv

#create project folder
mkdir auto-onboarding
cd auto-onboarding

# Create a new virtual environment
virtualenv venv 
source venv/bin/activate

# Install Django and other dependencies
pip install django

pip install requests
pip install argparse
pip install msal


# Create the Django project
django-admin startproject onboarding .

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Collect static files
#python manage.py collectstatic

# Create a symbolic link to the static files
#sudo ln -s /usr/bin/myproject/static /var/www/html/static

# Restart the Nginx service
#sudo systemctl restart nginx

# Start the development server
#python manage.py runserver


# Create the project directory


# Create the app directory
mkdir onboarding/templates
pwd

# Copy the template file to the app directory
cp ../src/create_user.html onboarding/templates/

# Copy the view file to the app directory
cp ../src/create_user_view.py onboarding/views.py

# Copy the create_user.py file to the project directory
cp ../src/create_user.py .

# Add the view to the urls.py file
echo "from django.urls import path
from .views import create_user

urlpatterns = [
    path('create_user/', create_user, name='create_user'),
]
" >> onboarding/urls.py

# Add the app to the settings.py file
echo "INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'onboarding',
]
" >> onboarding/settings.py

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start the development server
#python manage.py runserver

