import \
    os

import \
    django
from celery import \
    Celery

from .mail import \
    async_send_mail

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cms.settings")
django.setup()

app = Celery('django_celery')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

__all__ = (
    "async_send_mail"
)
