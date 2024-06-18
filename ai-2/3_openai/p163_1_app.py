import openai
import json

def response_from_ChatAI(user_content, r_num=1):
    messages = [
        {"role": "user", "content": user_content}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1000,
        temperature=0.8,
        n=r_num
    )

    assistant_replies = []

    for choice in response.choices:
        assistant_replies.append(choice.message['content'])

    return assistant_replies

while True:
    user_input = input("Q : ")
    if user_input.lower() in ['q', 'ㅂ']:
        break
    else:
        res = response_from_ChatAI(user_input)
        for reply in res:
            print("A : ", reply, end="\n\n")