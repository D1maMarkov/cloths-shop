import smtplib
from datetime import timedelta
from email.message import EmailMessage

from celery import Celery
from settings import settings
from utils.dependencies import user_repository_dependency as repository

celery = Celery("tasks", broker="redis://127.0.0.1:6379")


@celery.task
def send_mail(email, code, token):
    msg = EmailMessage()
    msg["Subject"] = "подтверждение почты"
    msg["From"] = settings.BACKEND_EMAIL
    msg["To"] = email

    msg.set_content(
        f"""
    <div>
    <a href="http:127.0.0.1:4000/confirm-email/{token}">ссылка для подтверждения почты</a>

    <h3>код для подтверждения: {code}</h3>
    </div>
    """,
        subtype="html",
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(settings.BACKEND_EMAIL, settings.BACKEND_EMAIL_PASSWORD)
        smtp.send_message(msg)


@celery.task
async def delete_inactive_users():
    await repository.delete_inactive_users()


celery.conf.beat_schedule = {
    "delete-inactive-users": {
        "task": "tasks.tasks.delete_inactive_users",
        "schedule": timedelta(days=1),
    },
}

# celery -A tasks.tasks beat -l info
# celery -A tasks.tasks worker -l INFO --pool=solo
