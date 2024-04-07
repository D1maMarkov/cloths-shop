import smtplib
from email.message import EmailMessage

from celery import Celery
from web_api.config import get_settings

celery = Celery("email", broker=get_settings().CELERY_BROKER_URL)


@celery.task
def send_mail(email: str, code: str, token: str, settings: dict):
    msg = EmailMessage()
    msg["Subject"] = "подтверждение почты"
    msg["From"] = settings["backend_email"]
    msg["To"] = email

    text = f"""
    <div>
    <a href="http://127.0.0.1:4200/confirm-email/{token}">ссылка для подтверждения почты</a>

    <h3>код для подтверждения: {code}</h3>
    </div>
    """

    msg.set_content(
        text,
        subtype="html",
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", settings["port"]) as smtp:
        smtp.login(settings["backend_email"], settings["backend_email_password"])
        smtp.send_message(msg)
