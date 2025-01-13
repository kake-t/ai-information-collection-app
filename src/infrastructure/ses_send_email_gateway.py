from typing import Any

import boto3

from src.domain.entities.send_email import SendEmailRequest
from src.domain.gateway.send_email_gateway import SendEmailGateway
from src.infrastructure.config import AwsConfig


class SesSendEmailGateway(SendEmailGateway):
    _CHARSET = "UTF-8"

    def __init__(self, aws_config: AwsConfig) -> None:
        self._aws_config = aws_config

    def send_email(self, request: SendEmailRequest) -> Any:
        source = request.source
        destination = request.destination
        subject = request.subject
        body = request.body

        ses = boto3.client(
            "ses",
            region_name=self._aws_config.resion,
        )
        ses.verify_email_identity(EmailAddress=source)
        try:
            response = ses.send_email(
                Source=source,
                Destination={"ToAddresses": [destination]},
                Message={
                    "Subject": {"Data": subject, "Charset": self._CHARSET},
                    "Body": {"Text": {"Data": body, "Charset": self._CHARSET}},
                },
            )

        except Exception as e:
            raise Exception(f"SES send mail error: {str(e)}")

        return response
