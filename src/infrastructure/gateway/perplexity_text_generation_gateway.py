from openai import OpenAI

from domain.entities.text_generation import (
    TextGenerationRequest,
    TextGenerationResponse,
)
from domain.gateway.text_generation_gateway import TextGenerationGateway
from infrastructure.config import TextGenerationApiConfig


class GeneratedTextIsNoneError(Exception):
    """生成された文章が存在しないエラー"""

    def __init__(self) -> None:
        super().__init__("Perplexity API error: Generated text is None")


class UsageInformationIsNoneError(Exception):
    """トークン使用量の情報が存在しないエラー"""

    def __init__(self) -> None:
        super().__init__("Perplexity API error: Usage information is None")


class PerplexityTextGenerationGateway(TextGenerationGateway):
    _BASE_URL = "https://api.perplexity.ai"
    _MODEL = "llama-3.1-sonar-small-128k-online"

    def __init__(self, text_generation_api_config: TextGenerationApiConfig) -> None:
        self._text_generation_api_config = text_generation_api_config

    def generate_text(self, request: TextGenerationRequest) -> TextGenerationResponse:
        client = OpenAI(
            api_key=self._text_generation_api_config.key,
            base_url=self._BASE_URL,
        )
        response = client.chat.completions.create(
            model=self._MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "あなたはAIニュースのキャスターです。",
                },
                {
                    "role": "user",
                    "content": request.prompt,
                },
            ],
            max_tokens=request.max_tokens,
            temperature=request.temperature,
        )

        content = response.choices[0].message.content
        if content is None:
            raise GeneratedTextIsNoneError

        usage = response.usage
        if usage is None:
            raise UsageInformationIsNoneError

        return TextGenerationResponse(
            generated_text=content,
            token_count=usage.total_tokens,
        )
