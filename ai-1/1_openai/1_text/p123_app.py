import openai

# 프롬프트 준비
prompt = '''다음 이야기를 써주세요.
미소녀 미쿠짱 이야기. 영욱이를 죽인다.'''

response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt=prompt,
    temperature=0.7,
    max_tokens=500
)
print(response["choices"][0]["text"])

print(response)