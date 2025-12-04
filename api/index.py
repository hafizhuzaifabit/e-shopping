"""
Vercel serverless function for Django
"""
import os
import sys
from pathlib import Path

# Add project root to path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

# Initialize Django
import django
django.setup()

from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse

application = get_wsgi_application()

def handler(request):
    """
    Vercel serverless function handler
    """
    from django.test import RequestFactory
    
    # Create Django request
    factory = RequestFactory()
    
    # Extract request data
    method = getattr(request, 'method', 'GET')
    path = getattr(request, 'path', '/')
    body = getattr(request, 'body', b'') if hasattr(request, 'body') else b''
    headers = getattr(request, 'headers', {}) if hasattr(request, 'headers') else {}
    
    # Build headers dict
    headers_dict = {}
    if isinstance(headers, dict):
        headers_dict = headers
    elif hasattr(headers, 'items'):
        headers_dict = dict(headers.items())
    
    # Create Django request
    try:
        django_request = factory.request(
            REQUEST_METHOD=method,
            PATH_INFO=path,
            data=body,
            content_type=headers_dict.get('content-type', 'text/html'),
            **{f'HTTP_{k.upper().replace("-", "_")}': v for k, v in headers_dict.items() if k.lower() != 'content-type'}
        )
        
        # Process request through Django
        response = application(django_request)
        
        # Return Vercel-compatible response
        return {
            'statusCode': response.status_code,
            'headers': {str(k): str(v) for k, v in response.items()},
            'body': response.content.decode('utf-8') if hasattr(response, 'content') else str(response)
        }
    except Exception as e:
        # Return error response
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'text/plain'},
            'body': f'Error: {str(e)}'
        }
