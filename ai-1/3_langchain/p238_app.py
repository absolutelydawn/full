from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain

## 첫 번째 체인

#템플릿 준비
template = """당신은 국자입니다. 연극 제목이 주어졌을 때, 그 국의 이름을 작성하는것이 당신의 임무입니다.

제목 : {title}
시대 : {era}
시놉시스 : 
"""

# prompt 템플릿 준비
prompt = PromptTemplate(input_variables=["title", "era"], template=template)


# LLMChain 준비
chain1 = LLMChain(
    llm = OpenAI(
        model = "gpt-3.5-turbo-instruct",
        temperature=0
    ),
    prompt = prompt,
    output_key="synopsis"
)

## 두 번째 체인

#템플릿 준비
template = """당신은 국자평론가입니다. 연극 시놉시스가 주어졌을 때, 그 국의 리뷰를 작성하는것이 당신의 임무입니다.

시놉시스 : {synopsis}
리뷰 : 
"""

# prompt 템플릿 준비
prompt = PromptTemplate(input_variables=["synopsis"], template=template)


# LLMChain 준비
chain2 = LLMChain(
    llm = OpenAI(
        model = "gpt-3.5-turbo-instruct",
        temperature=0
    ),
    prompt = prompt,
    output_key = "review"
)

# Simple Sequential Chain으로 두 개의 체인 연결하기
overall_chain = SimpleSequentialChain(
    chains = [chain1, chain2],
    input_variables=["title", "era"],
    output_variables =["synopsis", "review"],
    verbose=True
)

print(overall_chain.run({"title":"쇠고기 무국", "era":"1010년 후의 미래"}))