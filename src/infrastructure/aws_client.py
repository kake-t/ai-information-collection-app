import boto3


def get_ses_client(region: str):
    return boto3.client(
        "ses",
        region_name=region,
    )
