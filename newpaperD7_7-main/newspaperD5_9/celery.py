import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 
                      'newspaperD5_9.settings')

app = Celery('newspaperD5_9')
app.config_from_object('django.conf:settings', namespace = 'CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_message_every_monday': {
        'task': 'tasks.send_message',
        'schedule': crontab(minute=0, hour=8, day_of_week='monday'),
    },
}