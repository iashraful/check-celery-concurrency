## Check Celery Concurrency

### Default Pool
Celery worker is not fully concurrent. It works based on the CPU available on the machine. It internally use `Prefork` to do that. Prefork implemented based on Python's default multiprocessing. It keeps aside the Python's GIL(Global Interpreter Lock) and fully leverage the multiprocessing available on the machine.  
**So, How we can achieve this concurrency?**

### How to Concurrency?
Celery worker works with these four execution pool.
* `Prefork`
* `Solo` 
* `Gevent`
* `Eventlet` 

Today it's about `Gevent` and `Eventlet`.  
Let's say you have no CPU bound tasks. Just thousands of HTTP calls. Then it's high time to use one of these two. So, I have created a RnD project for tesing the load of concurrency. So, let's get started.

### Materials
* FastAPI
    * Our API framework for today.
* Celery
    * Using for worker who will process our concurrent tasks.
* Locust
    * Load tesing framework. We will just call the API thousands time
* Flower
    * Monitoring for celery worker
* Redis
    * Redis as celery broker and backend

### Concurrency with `gevent`
* Install with `pip install gevent`
* Change the `docker-compose.yml` like following,
```
celery -A config.worker worker --pool=gevent --concurrency=500 --loglevel=INFO
```
* `--concurrency=500` means you can able to handle 500 concurrent tasks. So, you can update the value from here.

### Concurrency with `eventlet`
* Install with `pip install eventlet`
* Change the `docker-compose.yml` like following,
```
celery -A config.worker worker --pool=evemtlet --concurrency=500 --loglevel=INFO
```
* `--concurrency=500` means you can able to handle 500 concurrent tasks. So, you can update the value from here.

### How to run?
* `docker compose up --build -d`
* `http://localhost:8088` is the FastAPI application.
* `http://localhost:8089` is the Locust(Load tesing tool).
    * If you run on docker then you might need `http://api:8080` as a server url while configuring the Locust.
* `http://localhost:8090` is the Flower(Celery monitoring tool).

