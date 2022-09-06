from celery.schedules import crontab


CELERY_BEAT_SCHEDULE = {
    # "trigger_scheduled_task": {
    #     "task": "config.tasks.scheduled_task",
    #     # Run at everyday minute
    #     "schedule": crontab(minute="*/1"),
    # },
}
