from langchain.llms import OpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

llm = OpenAI(
    model="gpt-3.5-turbo-instruct",
    streaming = True,
    callbacks=[StreamingStdOutCallbackHandler()],
    verbose=True,
    temperature=0
)

resp = llm("슬픈 ChatGPT 생활을 가사로 만들어줘.")