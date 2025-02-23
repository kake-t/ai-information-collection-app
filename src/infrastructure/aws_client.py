from typing import Any

import boto3


def get_ses_client(region: str) -> Any:
    return boto3.client(
        "ses",
        region_name=region,
    )
