import sys
from openai import OpenAI
import os


client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    organization=os.environ["OPENAI_ORGANIZATION"],
    project=os.environ["OPENAI_PROJECT_ID"],
)


def handler(event, context):
    # リクエストの送信（新しいAPI形式）
    response = client.chat.completions.create(
        model="gpt-4",  # または "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello! How can I use OpenAI's API?"},
        ],
        max_tokens=100,
        temperature=0.7,
    )

    # 結果の出力（新しいレスポンス形式）
    print(response.choices[0].message.content)
    return "Hello from AWS Lambda using Python" + sys.version + "!"
