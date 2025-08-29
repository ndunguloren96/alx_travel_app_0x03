# alx_travel_app/celery.py
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings')

app = Celery('alx_travel_app')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in all installed apps' 'tasks.py' modules.
app.autodiscover_tasks()
