from locust import HttpUser, task


class CeleryTaskPoolTester(HttpUser):
    @task
    def get_data(self):
        self.client.get("/test-concurrency")
