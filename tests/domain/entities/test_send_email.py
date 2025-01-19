from datetime import datetime
from zoneinfo import ZoneInfo

from src.domain.entities.send_email import SendEmailRequest


def test_send_email_request():
    # arrange
    today = datetime.now(ZoneInfo("Asia/Tokyo")).strftime("%Y-%m-%d")
    # act
    send_email_request = SendEmailRequest(
        source="example@email.com", destination="test@email.com", body="test生成"
    )

    # assert
    assert send_email_request.subject == f"{today}のAIニュースです。"
