#!/bin/bash
# Deploy script for PythonAnywhere
# Run this in PythonAnywhere Console

echo "🚀 Starting deployment..."

# Navigate to project directory
echo "📂 Navigating to project directory..."
cd /home/nongnarok20123/bakery-django

# Stash any local changes to avoid conflicts
echo "🗃️  Stashing local changes..."
git stash

# Pull latest changes from GitHub
echo "📥 Pulling latest changes from GitHub..."
git pull origin main

# Navigate to Django project folder
echo "📁 Navigating to Django project folder..."
cd pstore

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Restart web app
echo "🔄 Restarting web app..."
touch /var/www/nongnarok20123_pythonanywhere_com_wsgi.py

echo "✅ Deployment completed!"
echo "🌐 Your website should now be updated with the latest mobile responsive design!"
