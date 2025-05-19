from usecase.send_email_usecase import SendEmailUsecase
from tests.mock.infrastructure.mock_send_email_gateway import MockSendEmailGateway


def test_send_email_usecase_success():
    # arrange
    mock_send_email_gateway = MockSendEmailGateway()
    usecase = SendEmailUsecase(send_email_gateway=mock_send_email_gateway)

    # act
    usecase.send_email(
        source="test@test.com",
        destination="example@example.com",
        generated_text="テストプロンプトです",
    )

    # assert
    # モックなので実際のメール送信は行われないが、エラーが発生しないことを確認
