from src.usecase.text_generation_usecase import TextGenerationUsecase
from tests.mock.infrastructure.mock_text_generation_gateway import (
    MockTextGenerationGateway,
)


def test_text_generation_usecase_success():
    # arrange
    mock_text_generation_gateway = MockTextGenerationGateway()
    usecase = TextGenerationUsecase(text_generation_gateway=mock_text_generation_gateway)
    prompt = "テストプロンプトです"
    max_tokens = 100
    temperature = 0.7

    # act
    response = usecase.generate(prompt=prompt, max_tokens=max_tokens, temperature=temperature)

    # assert
    assert response.generated_text == "モックで生成されたテキスト"
