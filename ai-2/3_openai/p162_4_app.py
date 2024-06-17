import openai
import json

messages = [
    {"role" : "user", "content" : "한글은 언제 만들어졌나요?"}

]

response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages=messages,
    max_tokens = 500,
    temperature=0.7,
    n = 3
)

print("응답 개수", len(response.choices))
for c in response.choices:
    print(c.message['content'])