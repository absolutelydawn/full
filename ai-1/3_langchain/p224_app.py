from langchain.prompts import PromptTemplate

multiple_input_prompt = PromptTemplate(
    input_variables=["adjective", "content"],
    template="{adjective} {content}이라고 하면?",
)
print(multiple_input_prompt.format(adjective="멋진", content="동물"))