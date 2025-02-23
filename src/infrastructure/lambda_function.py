from typing import Any

from src.domain.entities.text_generation import DEFAULT_MAX_TOKENS, DEFAULT_TEMPERATURE
from src.infrastructure.aws_client import get_ses_client
from src.infrastructure.config import ConfigurationReader
from src.infrastructure.gateway.perplexity_text_generation_gateway import (
    PerplexityTextGenerationGateway,
)
from src.infrastructure.gateway.ses_send_email_gateway import SesSendEmailGateway
from src.usecase.send_email_usecase import SendEmailUsecase
from src.usecase.text_generation_usecase import TextGenerationUsecase


def handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    try:
        config = ConfigurationReader.get_config()
        prompt = event.get("prompt")
        max_tokens = event.get("max_tokens", DEFAULT_MAX_TOKENS)
        temperature = event.get("temperature", DEFAULT_TEMPERATURE)

        if not prompt:
            return {
                "statusCode": 400,
                "body": {"error": "Prompt is reqsuired"},
            }

        email_source = config.email.source
        email_destination = config.email.destination

        text_generation_gateway = PerplexityTextGenerationGateway(text_generation_api_config=config.text_genaration_api)
        usecase = TextGenerationUsecase(text_generation_gateway)
        # テキスト生成の実行
        text_generation_result = usecase.generate(prompt, max_tokens, temperature)
        generated_text = text_generation_result.generated_text

        email_gateway = SesSendEmailGateway(aws_client_ses=get_ses_client(region=config.aws.region))
        send_email_usecase = SendEmailUsecase(send_email_gateway=email_gateway)
        # email送信
        send_email_usecase.send_email(
            source=email_source,
            destination=email_destination,
            generated_text=generated_text,
        )

        return {
            "statusCode": 200,
            "body": {
                "generated_text": generated_text,
                "token_count": text_generation_result.token_count,
            },
        }

    except Exception as e:
        return {"statusCode": 500, "body": {"error": str(e)}}
