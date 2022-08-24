import os
from pathlib import Path
from pkgutil import iter_modules

from celery import Celery

BROKER = f"redis://{os.environ.get('REDIS_HOST', default='redis')}:{os.environ.get('REDIS_PORT', default=6379)}/2"
BACKEND = f"redis://{os.environ.get('REDIS_HOST', default='redis')}:{os.environ.get('REDIS_PORT', default=6379)}/2"

# BROKER = "redis://localhost:6382/2"
# BACKEND = "redis://localhost:6382/2"


def find_task_modules():
    api_path = [f"{Path().absolute()}/config"]
    return [module.name for module in iter_modules(api_path, prefix="config.")]


celery = Celery(__name__, broker=BROKER, backend=BACKEND)
celery.autodiscover_tasks(find_task_modules())


@celery.task(bind=True)
def debug_task(self):
    print("Debug task is running...")
