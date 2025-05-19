import os

import pytest
from moto import mock_aws

from domain.entities.send_email import SendEmailRequest
from infrastructure.aws_client import get_ses_client
from infrastructure.gateway.ses_send_email_gateway import SesSendEmailGateway


@mock_aws
def test_send_email_success():
    # 準備
    source = "source@example.com"
    destination = "destination@example.com"
    subject = "test title"
    body = "test body"

    request = SendEmailRequest(source=source, destination=destination, subject=subject, body=body)

    ses = get_ses_client(region=os.environ["AWS_REGION"])
    ses.verify_email_identity(EmailAddress=source)
    gateway = SesSendEmailGateway(aws_client_ses=ses)
    # 実行
    response = gateway.send_email(request)

    # 検証
    assert response["ResponseMetadata"]["HTTPStatusCode"] == 200


@mock_aws
def test_send_email_error():
    # 準備
    source = "invalid_email"  # 不正なメールアドレス
    destination = "destination@example.com"
    subject = "test title"
    body = "test body"

    request = SendEmailRequest(source=source, destination=destination, subject=subject, body=body)

    ses = get_ses_client(region=os.environ["AWS_REGION"])
    ses.verify_email_identity(EmailAddress=source)
    gateway = SesSendEmailGateway(aws_client_ses=ses)

    # 実行 & 検証
    with pytest.raises(Exception) as exc_info:
        gateway.send_email(request)
