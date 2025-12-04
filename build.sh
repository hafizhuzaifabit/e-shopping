#!/bin/bash
# Build script for Vercel
echo "Building Django application..."

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

echo "Build complete!"



