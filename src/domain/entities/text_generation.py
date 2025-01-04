from dataclasses import dataclass

DEFAULT_MAX_TOKENS = 1000
DEFAULT_TEMPERATURE = 0.7


@dataclass(frozen=True)
class TextGenerationRequest:
    prompt: str
    max_tokens: int = DEFAULT_MAX_TOKENS
    temperature: float = DEFAULT_TEMPERATURE


@dataclass(frozen=True)
class TextGenerationResponse:
    generated_text: str
    token_count: int
