from typing import Any

from domain.entities.text_generation import DEFAULT_MAX_TOKENS, DEFAULT_TEMPERATURE
from infrastructure.aws_client import get_ses_client
from infrastructure.config import ConfigurationReader
from infrastructure.gateway.perplexity_text_generation_gateway import (
    PerplexityTextGenerationGateway,
)
from infrastructure.gateway.ses_send_email_gateway import SesSendEmailGateway
from usecase.send_email_usecase import SendEmailUsecase
from usecase.text_generation_usecase import TextGenerationUsecase


def handler(event: dict[str, Any], _: Any) -> dict[str, Any]:
    try:
        config = ConfigurationReader.get_config()
        prompt = event.get("prompt")
        max_tokens = event.get("max_tokens", DEFAULT_MAX_TOKENS)
        temperature = event.get("temperature", DEFAULT_TEMPERATURE)

        if not prompt:
            return {
                "statusCode": 400,
                "body": {"error": "Prompt is required"},
            }

        email_source = config.email.source
        email_destination = config.email.destination

        text_generation_gateway = PerplexityTextGenerationGateway(text_generation_api_config=config.text_generation_api)
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

    except Exception as e:  # noqa: BLE001
        return {"statusCode": 500, "body": {"error": str(e)}}
    else:
        return {
            "statusCode": 200,
            "body": {
                "generated_text": generated_text,
                "token_count": text_generation_result.token_count,
            },
        }
