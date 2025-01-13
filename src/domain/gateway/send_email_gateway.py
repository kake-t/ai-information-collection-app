from typing import Protocol

from src.domain.entities.send_email import (
    SendEmailRequest,
)


class SendEmailGateway(Protocol):
    def send_email(self, request: SendEmailRequest) -> None: ...
