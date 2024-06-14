from langchain.prompts import PromptTemplate

one_input_prompt = PromptTemplate(
    input_variables=["content"],
    template="멋진 {content}이라고 하면?",
)
print(one_input_prompt.format(content="동물"))