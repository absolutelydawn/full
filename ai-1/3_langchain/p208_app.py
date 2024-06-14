from langchain.agents import load_tools
from langchain.llms import OpenAI
from langchain.agents import initialize_agent
import os

serpapi_api_key = os.environ.get("SERPAPI_API_KEY")

tools = load_tools(["serpapi", "llm-math"], llm=OpenAI(
    model="gpt-3.5-turbo-instruct",
    temperature=0
    ),
    serpapi_api_key = serpapi_api_key
)

agent = initialize_agent(
    agent="zero-shot-react-description",
    llm=OpenAI(
        model="gpt-3.5-turbo-instruct",
        temperature=0
    ),
    tools=tools,
    verbose=True
)

agent.run("123 * 4 를 계산기로 계산하세요. 답변을 한국어로 알려줘.")
print('-' * 50)

agent.run("답변을 한국어로 알려줘. 야마돌게 하는 야바문에게 전달할 말을 생성해줘.")
print('-' * 50)