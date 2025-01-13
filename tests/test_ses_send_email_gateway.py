import os

import pytest
from moto import mock_aws

from src.domain.entities.send_email import SendEmailRequest
from src.infrastructure.ses_send_email_gateway import SesSendEmailGateway
from src.infrastructure.config import AwsConfig

AWS_RESION = "ap-northeast-1"


@pytest.fixture
def gateway():
    # 環境変数のセットアップ
    os.environ.pop("AWS_PROFILE", None)
    return SesSendEmailGateway(AwsConfig(resion=AWS_RESION))


@mock_aws
def test_send_email_success(gateway):
    # 準備
    source = "source@example.com"
    destination = "destination@example.com"
    subject = "test title"
    body = "test body"

    request = SendEmailRequest(
        source=source, destination=destination, subject=subject, body=body
    )

    # 実行
    response = gateway.send_email(request)

    # 検証
    assert response["ResponseMetadata"]["HTTPStatusCode"] == 200


@mock_aws
def test_send_email_error(gateway):
    # 準備
    source = "invalid_email"  # 不正なメールアドレス
    destination = "destination@example.com"
    subject = "test title"
    body = "test body"

    request = SendEmailRequest(
        source=source, destination=destination, subject=subject, body=body
    )

    # 実行 & 検証
    with pytest.raises(Exception) as exc_info:
        gateway.send_email(request)
    assert "SES send mail error" in str(exc_info.value)
