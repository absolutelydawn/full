import asyncio
import nest_asyncio
import time
from langchain.llms import OpenAI

nest_asyncio.apply()

async def async_generate(llm):
    resp = await llm.agenerate(["안녕하세요!"])
    print(resp.generations[0][0].text)

async def generate_concurrently():
    llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.9)

    tasks = [async_generate(llm) for _ in range(10)]
    await asyncio.gather(*tasks)

s = time.perf_counter()

asyncio.run(generate_concurrently())

elapsed = time.perf_counter() -s
print(f"{elapsed:0.2f} seconds")