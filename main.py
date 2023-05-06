from config.tasks import call_thirdparty_api, data_processing_task
from celery import chain, group
from time import time
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/test-concurrency")
async def call_github_api():
    call_thirdparty_api.delay()
    return {"message": "API is calling..."}


@app.get("/celery-chains/{num_tasks}/{num_groups}/{num_iteration}")
async def celery_multiprocessing(num_tasks: int, num_groups: int, num_iteration: int):
    task_payload = {"length": num_iteration}

    _groups = []
    for _ in range(num_groups):
        _tasks = []
        for _ in range(num_tasks):
            _tasks.append(data_processing_task.s(task_payload))
        _groups.append(group(*_tasks))
    print(f"{num_groups} groups created.")

    for g in _groups:
        start = time()
        g.apply_async()
        g()
        end = time()
        print(f"Time difference: {end-start}")

    return {"message": "Look at the celery worker console."}
