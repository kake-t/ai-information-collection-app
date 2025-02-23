from typing import Any

import boto3


def get_ses_client(region: str) -> Any:  # noqa: ANN401
    return boto3.client(
        "ses",
        region_name=region,
    )
