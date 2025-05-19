from typing import Protocol

from domain.entities.send_email import (
    SendEmailRequest,
)


class SendEmailGateway(Protocol):
    def send_email(self, request: SendEmailRequest) -> None: ...
