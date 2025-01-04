from src.domain.entities.text_generation import (
    TextGenerationRequest,
    TextGenerationResponse,
)
from src.domain.service_interfaces.text_generation_service import TextGenerationService


class TextGenerationUseCase:
    def __init__(self, text_generation_service: TextGenerationService):
        self._text_generation_service = text_generation_service

    def generate(
        self, prompt: str, max_tokens: int, temperature: float
    ) -> TextGenerationResponse:
        request = TextGenerationRequest(
            prompt=prompt, max_tokens=max_tokens, temperature=temperature
        )
        return self._text_generation_service.generate_text(request)
