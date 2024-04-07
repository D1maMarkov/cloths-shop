from datetime import timedelta

from asgiref.sync import async_to_sync
from celery import Celery
from infrastructure.persistence.repositories.user_repository import UserRepository
from web_api.config import get_settings
from web_api.depends.get_db import get_db

celery = Celery("tasks", broker=get_settings().CELERY_BROKER_URL)


def get_repository() -> UserRepository:
    db = get_db().__anext__()
    return UserRepository(db)


@celery.task
def delete_inactive_users():
    repository = get_repository()
    async_to_sync(repository.delete_inactive_users)()


celery.conf.beat_schedule = {
    "delete-inactive-users": {
        "task": "tasks.delete_inactive_users",
        "schedule": timedelta(days=1),
    },
}
