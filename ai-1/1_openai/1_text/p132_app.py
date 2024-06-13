import openai

# 채팅 메세지 리스트 준비
messages = [
    {"role": "system", "content":"오타를 수정해 주세요."},
    {"role": "user", "content": "설명참고 설참 . 이양기가 참 재미있다."}
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=0
)

print(response)
print('-' * 50)
print(response["choices"][0]["message"]["content"])