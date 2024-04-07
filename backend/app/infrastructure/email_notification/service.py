from application.common.email_notification import EmailNotificationServiceInterface
from infrastructure.email_notification.backend_tasks import send_mail
from infrastructure.email_notification.email_settings import EmailSettings


class EmailNotificationService(EmailNotificationServiceInterface):
    def __init__(self, settings: EmailSettings) -> None:
        self.settings = settings

    def send_mail(self, email: str, code: str, token: str) -> None:
        send_mail.delay(email, code, token, self.settings.model_dump())
