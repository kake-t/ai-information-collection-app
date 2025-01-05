import os

from openai import OpenAI

from src.domain.entities.text_generation import (
    TextGenerationRequest,
    TextGenerationResponse,
)
from src.domain.gateway.text_generation_gateway import TextGenerationGateway


class PerplexityTextGenerationGateway(TextGenerationGateway):
    _BASE_URL = "https://api.perplexity.ai"
    _MODEL = "llama-3.1-sonar-small-128k-online"

    def __init__(self):
        pass

    def generate_text(self, request: TextGenerationRequest) -> TextGenerationResponse:
        client = OpenAI(
            api_key=os.environ["PERPLEXITY_API_KEY"],
            base_url=self._BASE_URL,
        )
        messages = [
            {
                "role": "system",
                "content": "あなたはAIニュースのキャスターです。",
            },
            {"role": "user", "content": request.prompt},
        ]
        try:
            response = client.chat.completions.create(
                model=self._MODEL,
                messages=messages,
                max_tokens=request.max_tokens,
                temperature=request.temperature,
            )

            return TextGenerationResponse(
                generated_text=response.choices[0].message.content,
                token_count=response.usage.total_tokens,
            )
        except Exception as e:
            raise Exception(f"Perplexity API error: {str(e)}")
