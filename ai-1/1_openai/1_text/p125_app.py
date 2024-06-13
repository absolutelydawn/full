import openai

prompt = "야바위의 제왕, 말바꿈의 정수 야바문과 비트 교육생간의 배틀로얄 이야기를 알려주세요."

response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt=prompt,
    temperature=0,
    max_tokens=1500
)

print(response["choices"][0]["text"])

print(response)