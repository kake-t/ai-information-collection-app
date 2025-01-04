from src.infrastructure.lambda_function import handler
import os


def test_handler():
    print(os.environ["PERPLEXITY_API_KEY"])
    event = {
        "prompt": "昨日のAIに関するニュースを教えて下さい。冒頭に機能の年月日を出力してください。"
    }
    context = {}
    result = handler(event, context)
    print(result["body"])
    assert result["statusCode"] == 200
