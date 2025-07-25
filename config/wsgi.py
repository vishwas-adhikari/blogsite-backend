# backend/config/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

# --- THIS IS THE FIX ---
# Change 'backend.settings' to 'config.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()