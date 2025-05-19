from domain.entities.send_email import SendEmailRequest
from domain.gateway.send_email_gateway import SendEmailGateway


class MockSendEmailGateway(SendEmailGateway):
    def send_email(self, request: SendEmailRequest) -> None:
        pass  # モックなので実際の処理は行わない
