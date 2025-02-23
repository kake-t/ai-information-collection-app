from typing import Any

from src.domain.entities.send_email import SendEmailRequest
from src.domain.gateway.send_email_gateway import SendEmailGateway


class SesSendEmailGateway(SendEmailGateway):
    _CHARSET = "UTF-8"

    def __init__(self, aws_client_ses: Any) -> None:
        self._ses = aws_client_ses

    def send_email(self, request: SendEmailRequest) -> Any:
        source = request.source
        destination = request.destination
        subject = request.subject
        body = request.body

        return self._ses.send_email(
            Source=source,
            Destination={"ToAddresses": [destination]},
            Message={
                "Subject": {"Data": subject, "Charset": self._CHARSET},
                "Body": {"Text": {"Data": body, "Charset": self._CHARSET}},
            },
        )
