from src.lambda_function import handler


def test_handler():
    event = {}
    context = {}
    handler(event, context)
