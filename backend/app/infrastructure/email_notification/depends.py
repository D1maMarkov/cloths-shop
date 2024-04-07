from fastapi import Depends

from .email_settings import EmailSettings, get_email_settings
from .service import EmailNotificationService


def get_email_service(settings: EmailSettings = Depends(get_email_settings)) -> EmailNotificationService:
    email_notification_service = EmailNotificationService(settings)
    return email_notification_service
