from langchain.llms import OpenAI

llm = OpenAI(
    model = "gpt-3.5-turbo-instruct",
    temperature=0
)

result = llm("고양이 울음소리는?")
print(result)

result = llm.generate(["고양이 울음소리는?","개구리의 울음소리는?", "오이의 울음소리는?"])
print("result 0 : ", result.generations[0][0].text)
print("result 1 : ", result.generations[1][0].text)
print("result 2 : ", result.generations[2][0].text)

print("llm_output: ", result.llm_output)