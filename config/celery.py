import os
from pathlib import Path
from pkgutil import iter_modules

from celery import Celery
from config.beat_schedule import CELERY_BEAT_SCHEDULE

BROKER = f"redis://{os.environ.get('REDIS_HOST', default='redis')}:{os.environ.get('REDIS_PORT', default=6379)}/1"
BACKEND = f"redis://{os.environ.get('REDIS_HOST', default='redis')}:{os.environ.get('REDIS_PORT', default=6379)}/2"
REDBEAT_BACKEND = f"redis://{os.environ.get('REDIS_HOST', default='redis')}:{os.environ.get('REDIS_PORT', default=6379)}/3"


def find_task_modules():
    api_path = [f"{Path().absolute()}/config"]
    return [module.name for module in iter_modules(api_path, prefix="config.")]


celery = Celery(__name__, broker=BROKER, backend=BACKEND)
celery.autodiscover_tasks(find_task_modules())
celery.conf.beat_schedule = CELERY_BEAT_SCHEDULE
celery.conf.worker_send_task_events = True
celery.conf.task_send_sent_event = True
celery.conf.redbeat_redis_url = REDBEAT_BACKEND


@celery.task(bind=True)
def debug_task(self):
    print("Debug task is running...")
