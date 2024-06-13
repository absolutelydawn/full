import openai

text = "이것은 테스트입니다."

response = openai.Embedding.create(
    input = [text],
    model = "text-embedding-ada-002"
)

print(len(response["data"][0]["embedding"]))
print(response["data"][0]["embedding"])

# print(response)