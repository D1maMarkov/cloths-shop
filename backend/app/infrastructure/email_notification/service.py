from .backend_tasks import send_mail
from .email_settings import EmailSettings


class EmailNotificationService:
    def __init__(self, settings: EmailSettings) -> None:
        self.settings = settings

    def send_mail(self, email: str, code: str, token: str) -> None:
        send_mail.delay(email, code, token, self.settings.model_dump())
