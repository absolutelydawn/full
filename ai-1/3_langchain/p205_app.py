from langchain.llms import OpenAI

llm = OpenAI(
    model_name="gpt-3.5-turbo-instruct",
    temperature = 0.9,
)

print(llm("컴퓨터 게임을 만드는 새로운 한국어 회사명을 하나 제안해 주세요."))