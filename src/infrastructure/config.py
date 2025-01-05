from dataclasses import dataclass
import os
from functools import lru_cache


@dataclass(frozen=True)
class AwsConfig:
    resion: str


@dataclass(frozen=True)
class TextGenerationApiConfig:
    text_generation_api_key: str


@dataclass
class Config:
    aws: AwsConfig
    text_genaration_api: TextGenerationApiConfig


class ConfigurationError(Exception):
    """設定エラーを表すカスタム例外"""

    pass


class ConfigurationReader:
    @staticmethod
    def get_env_var(key: str) -> str:
        """環境変数を取得し、存在しない場合は例外を発生させる"""
        value = os.getenv(key)
        if value is None:
            raise ConfigurationError(f"環境変数 {key} が設定されていません")
        return value

    @staticmethod
    def get_env_int(key: str) -> int:
        """環境変数を整数として取得する"""
        value = ConfigurationReader.get_env_var(key)
        try:
            return int(value)
        except ValueError:
            raise ConfigurationError(
                f"環境変数 {key} は有効な整数ではありません: {value}"
            )

    @staticmethod
    @lru_cache(maxsize=1)
    def get_config() -> Config:
        """設定を読み込んでConfigオブジェクトを返す"""
        try:
            aws_config = AwsConfig(
                resion=ConfigurationReader.get_env_var("AWS_REGION"),
            )

            text_generation_api_config = TextGenerationApiConfig(
                text_generation_api_key=ConfigurationReader.get_env_var(
                    "PERPLEXITY_API_KEY"
                ),
            )

            return Config(
                aws=aws_config,
                text_genaration_api=text_generation_api_config,
            )
        except Exception as e:
            raise ConfigurationError(
                f"設定の読み込み中にエラーが発生しました: {str(e)}"
            )
