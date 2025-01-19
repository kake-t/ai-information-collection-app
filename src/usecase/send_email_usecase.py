from src.domain.gateway.send_email_gateway import SendEmailGateway
from src.domain.entities.send_email import SendEmailRequest


class SendEmailUsecase:
    def __init__(self, send_email_gateway: SendEmailGateway) -> None:
        self._send_email_gateway = send_email_gateway

    def send_email(self, source: str, destination: str, generated_text: str) -> None:
        request = SendEmailRequest(
            source=source, destination=destination, body=generated_text
        )
        return self._send_email_gateway.send_email(request)
