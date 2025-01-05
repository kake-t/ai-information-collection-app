import boto3

from src.domain.entities.send_email import SendEmailRequest
from src.domain.gateway.send_email_gateway import SendEmailGateway
from src.infrastructure.config import AwsConfig


class SesSendEmailGateway(SendEmailGateway):
    _CHARSET = "UTF-8"

    def __init__(self, aws_config: AwsConfig) -> None:
        self._aws_config = aws_config

    def send_email(self, request: SendEmailRequest) -> None:
        ses = boto3.client(
            "ses",
            region_name=self._aws_config.resion,
        )
        try:
            _ = ses.send_email(
                Source=request.source,
                Destination={"ToAddresses": [request.destination]},
                Message={
                    "Subject": {"Data": request.subject, "Charset": self._CHARSET},
                    "Body": {"Text": {"Data": request.body, "Charset": self._CHARSET}},
                },
            )

        except Exception as e:
            raise Exception(f"SES send mail error: {str(e)}")
