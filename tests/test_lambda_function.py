from src.infrastructure.lambda_function import handler


def test_handler():
    event = {"prompt": "今日のAIに関するニュースを教えて下さい。"}
    context = {}
    result = handler(event, context)
    print(result["body"])
