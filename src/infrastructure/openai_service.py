import os

from openai import OpenAI

from src.domain.entities.text_generation import (
    TextGenerationRequest,
    TextGenerationResponse,
)
from src.domain.service_interfaces.text_generation_service import TextGenerationService


class OpenAIService(TextGenerationService):
    def __init__(self):
        pass

    def generate_text(self, request: TextGenerationRequest) -> TextGenerationResponse:
        client = OpenAI(
            api_key=os.environ["OPENAI_API_KEY"],
            organization=os.environ["OPENAI_ORGANIZATION"],
            project=os.environ["OPENAI_PROJECT_ID"],
        )
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
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

            return TextGenerationResponse(
                generated_text=response.choices[0].message.content,
                token_count=response.usage.total_tokens,
            )
        except Exception as e:
            raise Exception(f"OpenAI API error: {str(e)}")
