import time
from .celery import celery as celery_app
import requests


@celery_app.task
def call_thirdparty_api():
    response = requests.get("https://api.github.com")
    if response and response.status_code == 200:
        print("Success")
    else:
        print("Response Failed")

    time.sleep(10)


@celery_app.task
def data_processing_task(payload: dict):
    print(f"Task received at {time.time()}")
    total_items = 0
    # Just looping over the data. Fake process
    for _ in range(payload.get("length", 0)):
        total_items += 1
    print(f"Total count: {total_items}")


@celery_app.task
def scheduled_task():
    print("Scheduled Task Started.")
    time.sleep(5)
    print("Scheduled Tasks Ended.")
