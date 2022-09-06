import time
from .celery import celery as celery_app
from celery import shared_task
import requests


@celery_app.task
def call_thirdparty_api():
    response = requests.get("https://api.github.com")
    if response and response.status_code == 200:
        print("Success")
    else:
        print("Response Failed")

    time.sleep(10)


@shared_task
def scheduled_task():
    print("Scheduled Task Started.")
    time.sleep(5)
    print("Scheduled Tasks Ended.")
