from celery import Celery

app = Celery(
    'currency_converter',
    include=['fetcher.tasks']
)

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
