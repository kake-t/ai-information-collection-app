from dataclasses import dataclass


@dataclass(frozen=True)
class SendEmailRequest:
    source: str
    destination: str
    subject: str
    body: str
