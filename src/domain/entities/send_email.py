from dataclasses import dataclass, field
from datetime import datetime
from zoneinfo import ZoneInfo


@dataclass(frozen=True)
class SendEmailRequest:
    source: str
    destination: str
    body: str
    subject: str = field(
        default_factory=lambda: f"{datetime.now(ZoneInfo('Asia/Tokyo')).strftime('%Y-%m-%d')}のAIニュースです。"
    )
