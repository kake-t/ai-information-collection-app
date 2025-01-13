import os
from unittest.mock import MagicMock
import pytest

from src.domain.entities.text_generation import (
    TextGenerationRequest,
    TextGenerationResponse,
)
from src.infrastructure.perplexity_text_generation_gateway import (
    PerplexityTextGenerationGateway,
)
from src.infrastructure.config import ConfigurationReader


@pytest.fixture
def gateway():
    # 環境変数のセットアップ
    os.environ["PERPLEXITY_API_KEY"] = "test-api-key"
    os.environ["AWS_REGION"] = "ap-northeast-1"
    config = ConfigurationReader.get_config().text_genaration_api
    return PerplexityTextGenerationGateway(text_generation_api_config=config)


def test_generate_text_success(mocker, gateway):
    """正常処理のテスト"""
    # 準備
    expected_text = "本日のAIニュースはXXXXです。"
    expected_token_count = 50

    mock_client = MagicMock()
    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content=expected_text))],
        usage=MagicMock(total_tokens=expected_token_count),
    )
    mocker.patch(
        "src.infrastructure.perplexity_text_generation_gateway.OpenAI",
        return_value=mock_client,
    )

    request = TextGenerationRequest(
        prompt="テストプロンプト", max_tokens=100, temperature=0.7
    )

    # 実行
    response = gateway.generate_text(request)

    # 検証
    assert isinstance(response, TextGenerationResponse)
    assert response.generated_text == expected_text
    assert response.token_count == expected_token_count

    # APIクライアントの呼び出し検証
    mock_client.chat.completions.create.assert_called_once_with(
        model=gateway._MODEL,
        messages=[
            {
                "role": "system",
                "content": "あなたはAIニュースのキャスターです。",
            },
            {"role": "user", "content": request.prompt},
        ],
        max_tokens=request.max_tokens,
        temperature=request.temperature,
    )


def test_generate_text_api_error(mocker, gateway):
    """apiエラーのテスト"""
    # 準備
    mock_client = MagicMock()
    mock_client.chat.completions.create.side_effect = Exception("API Error")
    mocker.patch(
        "src.infrastructure.perplexity_text_generation_gateway.OpenAI",
        return_value=mock_client,
    )

    request = TextGenerationRequest(
        prompt="テストプロンプト", max_tokens=100, temperature=0.7
    )

    # 実行 & 検証
    with pytest.raises(Exception) as exc_info:
        gateway.generate_text(request)
    assert "Perplexity API error: API Error" in str(exc_info.value)
