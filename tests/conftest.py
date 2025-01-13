import os

import pytest


@pytest.fixture(scope="session", autouse=True)
def set_env_global():
    # 環境変数のセットアップ
    os.environ.pop("AWS_PROFILE", None)
    os.environ["PERPLEXITY_API_KEY"] = "test-api-key"
    os.environ["AWS_REGION"] = "ap-northeast-1"
