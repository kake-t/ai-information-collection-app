from src.domain.gateway.text_generation_gateway import TextGenerationGateway
from src.domain.entities.text_generation import (
    TextGenerationRequest,
    TextGenerationResponse,
)


class MockTextGenerationGateway(TextGenerationGateway):
    def generate_text(self, request: TextGenerationRequest) -> TextGenerationResponse:
        return TextGenerationResponse(
            generated_text="モックで生成されたテキスト", token_count=100
        )
