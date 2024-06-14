from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

chat_llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0
)

message = [
    HumanMessage(content="고양이 울음소리는?")
]
result = chat_llm(message)
print(result)

messages_list = [
    [HumanMessage(content="고양이 울음소리는?")],
    [HumanMessage(content="피카츄 울음소리는?")],
]
result = chat_llm.generate(messages_list)

print("result 0 : ", result.generations[0][0].text)
print("result 0 : ", result.generations[1][0].text)

print("llm_output : ", result.llm_output)