import os
from dataclasses import dataclass
from functools import lru_cache


@dataclass(frozen=True)
class AwsConfig:
    region: str


@dataclass(frozen=True)
class TextGenerationApiConfig:
    key: str


@dataclass(frozen=True)
class EmailConfig:
    source: str
    destination: str


@dataclass(frozen=True)
class Config:
    aws: AwsConfig
    text_generation_api: TextGenerationApiConfig
    email: EmailConfig


class ConfigurationRequiredError(ValueError):
    """環境変数が設定されていない"""

    def __init__(self, key: str) -> None:
        super().__init__(f"環境変数 {key} が設定されていません")


class InvalidIntegerFormatError(ValueError):
    """環境変数の値が整数ではない"""

    def __init__(self, key: str, value: str) -> None:
        super().__init__(f"環境変数 {key} は有効な整数ではありません: {value}")


class ConfigurationReader:
    @staticmethod
    def get_env_var(key: str) -> str:
        """環境変数を取得し、存在しない場合は例外を発生させる"""
        value = os.getenv(key)
        if value is None:
            raise ConfigurationRequiredError(key)
        return value

    @staticmethod
    def get_env_int(key: str) -> int:
        """環境変数を整数として取得する"""
        value = ConfigurationReader.get_env_var(key)
        try:
            return int(value)
        except ValueError as e:
            raise InvalidIntegerFormatError(key, str(value)) from e

    @staticmethod
    @lru_cache(maxsize=1)
    def get_config() -> Config:
        """設定を読み込んでConfigオブジェクトを返す"""
        aws_config = AwsConfig(
            region=ConfigurationReader.get_env_var("AWS_REGION"),
        )

        text_generation_api_config = TextGenerationApiConfig(
            key=ConfigurationReader.get_env_var("PERPLEXITY_API_KEY"),
        )

        email_config = EmailConfig(
            source=ConfigurationReader.get_env_var("EMAIL_SOURCE"),
            destination=ConfigurationReader.get_env_var("EMAIL_DESTINATION"),
        )

        return Config(
            aws=aws_config,
            text_generation_api=text_generation_api_config,
            email=email_config,
        )
