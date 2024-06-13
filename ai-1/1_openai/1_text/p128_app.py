import openai

# 채팅 메시지 리스트 준비
messages = [
    {"role": "system", "content": "아카네는 여고생 여동생 캐릭터의 채팅 AI입니다. 남동생과 대화합니다."},
    {"role": "user", "content": "안녕!"},
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
)

print(response)
print('-' * 50)
print(response["choices"][0]["message"]["content"])