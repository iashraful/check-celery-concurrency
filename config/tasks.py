from .worker import celery as celery_app
import requests


@celery_app.task
def call_thirdparty_api():
    response = requests.get("https://api.github.com")
    if response and response.status_code == 200:
        print("Success")
