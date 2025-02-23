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


class _ConfigurationError(Exception):
    """設定エラーを表すカスタム例外"""


class ConfigurationReader:
    @staticmethod
    def get_env_var(key: str) -> str:
        """環境変数を取得し、存在しない場合は例外を発生させる"""
        value = os.getenv(key)
        if value is None:
            raise _ConfigurationError(f"環境変数 {key} が設定されていません")
        return value

    @staticmethod
    def get_env_int(key: str) -> int:
        """環境変数を整数として取得する"""
        value = ConfigurationReader.get_env_var(key)
        try:
            return int(value)
        except ValueError:
            raise _ConfigurationError(f"環境変数 {key} は有効な整数ではありません: {value}")

    @staticmethod
    @lru_cache(maxsize=1)
    def get_config() -> Config:
        """設定を読み込んでConfigオブジェクトを返す"""
        try:
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
        except Exception as e:
            raise _ConfigurationError(f"設定の読み込み中にエラーが発生しました: {e!s}")
