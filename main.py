from config.tasks import call_thirdparty_api

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/test-concurrency")
async def call_github_api():
    call_thirdparty_api.delay()
    return {"message": "API is calling..."}
