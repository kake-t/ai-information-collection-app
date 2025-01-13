from src.infrastructure.lambda_function import handler


def test_handler():
    event = {
        "prompt": "昨日のAIに関するニュースを教えて下さい。冒頭に昨日の年月日を出力してください。",
        "max_tokens": 1000,
        "temperature": 0.7,
    }
    context = {}
    result = handler(event, context)
    print(result["body"])
    assert result["statusCode"] == 200
