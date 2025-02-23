from typing import Protocol

from src.domain.entities.text_generation import (
    TextGenerationRequest,
    TextGenerationResponse,
)


class TextGenerationGateway(Protocol):
    def generate_text(self, request: TextGenerationRequest) -> TextGenerationResponse: ...
