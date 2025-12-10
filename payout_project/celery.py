# Интеграция Celery
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'payout_project.settings')

app = Celery('payout_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()