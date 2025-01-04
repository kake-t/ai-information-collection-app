from typing import Any

from src.domain.entities.text_generation import DEFAULT_MAX_TOKENS, DEFAULT_TEMPERATURE
from src.usecase.text_generation_usecase import TextGenerationUseCase
from src.infrastructure.perplexity_gateway import PerplexityGateway


def handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    try:
        prompt = event.get("prompt")
        max_tokens = event.get("max_tokens", DEFAULT_MAX_TOKENS)
        temperature = event.get("temperature", DEFAULT_TEMPERATURE)

        if not prompt:
            return {
                "statusCode": 400,
                "body": {"error": "Prompt is reqsuired"},
            }

        openai_gateway = PerplexityGateway()
        usecase = TextGenerationUseCase(openai_gateway)

        # テキスト生成の実行
        result = usecase.generate(prompt, max_tokens, temperature)

        return {
            "statusCode": 200,
            "body": {
                "generated_text": result.generated_text,
                "token_count": result.token_count,
            },
        }

    except Exception as e:
        return {"statusCode": 500, "body": {"error": str(e)}}
