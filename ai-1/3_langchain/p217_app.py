import langchain
from langchain.llms import OpenAI

llm = OpenAI(
    model="gpt-3.5-turbo-instruct",
    temperature=0,
)
llm = OpenAI(
    model="gpt-3.5-turbo-instruct",
    cache=False
)


print(llm.generate(["지금 야바문의 심정을 알려줘."]))

print(llm.generate(["지금 야바문의 심정을 알려줘."]))