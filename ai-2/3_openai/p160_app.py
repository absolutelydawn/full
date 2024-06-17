import openai

messages = [
    {"role" : "user", "content" : "호주 수도는 어디인가요?"}

]

response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages=messages,
    max_tokens = 500,
    temperature=0.7,
    n = 1
)

assistent_reply = response.choices[0].message["content"]
print(assistent_reply)