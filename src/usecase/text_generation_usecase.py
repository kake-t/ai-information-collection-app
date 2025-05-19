from domain.entities.text_generation import (
    TextGenerationRequest,
    TextGenerationResponse,
)
from domain.gateway.text_generation_gateway import TextGenerationGateway


class TextGenerationUsecase:
    def __init__(self, text_generation_gateway: TextGenerationGateway) -> None:
        self._text_generation_gateway = text_generation_gateway

    def generate(self, prompt: str, max_tokens: int, temperature: float) -> TextGenerationResponse:
        request = TextGenerationRequest(prompt=prompt, max_tokens=max_tokens, temperature=temperature)
        return self._text_generation_gateway.generate_text(request)
