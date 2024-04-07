from typing import Protocol


class EmailNotificationServiceInterface(Protocol):
    def send_mail(self, email: str, code: str, token: str) -> None:
        raise NotImplementedError
