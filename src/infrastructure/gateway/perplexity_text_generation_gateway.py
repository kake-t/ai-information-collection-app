from openai import OpenAI

from src.domain.entities.text_generation import (
    TextGenerationRequest,
    TextGenerationResponse,
)
from src.domain.gateway.text_generation_gateway import TextGenerationGateway
from src.infrastructure.config import TextGenerationApiConfig


class PerplexityTextGenerationGateway(TextGenerationGateway):
    _BASE_URL = "https://api.perplexity.ai"
    _MODEL = "llama-3.1-sonar-small-128k-online"

    def __init__(self, text_generation_api_config: TextGenerationApiConfig):
        self._text_generation_api_config = text_generation_api_config

    def generate_text(self, request: TextGenerationRequest) -> TextGenerationResponse:
        client = OpenAI(
            api_key=self._text_generation_api_config.key,
            base_url=self._BASE_URL,
        )
        try:
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
                raise Exception("Generated text is None")

            usage = response.usage
            if usage is None:
                raise Exception("Usage information is None")

            return TextGenerationResponse(
                generated_text=content,
                token_count=usage.total_tokens,
            )
        except Exception as e:
            raise Exception(f"Perplexity API error: {e!s}")
