#!/bin/bash

# Install required packages
apt-get update
apt-get install -y python3-pip python3-dev nginx
./setup.sh

# Create a new nginx server block configuration
echo "server {
    listen 80;
    server_name *;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
    }

    location /static/ {
        alias /opt/auto-onboarding/static/;
    }
}" > /etc/nginx/sites-available/auto-onboarding

# Symlink the configuration to the sites-enabled directory
ln -s /etc/nginx/sites-available/auto-onboarding /etc/nginx/sites-enabled/

# Restart nginx
systemctl restart nginx

# Run the Django development server
cd /opt/auto-onboarding
python3 manage.py runserver 0.0.0.0:8000

