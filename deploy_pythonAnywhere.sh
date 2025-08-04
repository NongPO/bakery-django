#!/bin/bash
# Deploy script for PythonAnywhere
# Run this in PythonAnywhere Console

echo "🚀 Starting deployment..."

# Pull latest changes from GitHub
echo "📥 Pulling latest changes from GitHub..."
git pull origin main

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Restart web app (replace 'yourusername' with your actual username)
echo "🔄 Restarting web app..."
touch /var/www/yourusername_pythonanywhere_com_wsgi.py

echo "✅ Deployment completed!"
echo "🌐 Your website should now be updated with the latest mobile responsive design!"
