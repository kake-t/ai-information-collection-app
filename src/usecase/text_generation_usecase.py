from src.domain.entities.text_generation import (
    TextGenerationRequest,
    TextGenerationResponse,
)
from src.domain.gateway.text_generation_gateway import TextGenerationGateway


class TextGenerationUseCase:
    def __init__(self, text_generation_gateway: TextGenerationGateway):
        self._text_generation_gateway = text_generation_gateway

    def generate(
        self, prompt: str, max_tokens: int, temperature: float
    ) -> TextGenerationResponse:
        request = TextGenerationRequest(
            prompt=prompt, max_tokens=max_tokens, temperature=temperature
        )
        return self._text_generation_gateway.generate_text(request)
