import os
import textwrap

KAGI_API_KEY = os.environ["KAGI_API_KEY"]

api_url = "https://kagi.com/api/v0/summarize"
contents_url = "https://www.youtube.com/watch?v=BmYv8XGl-YU"
headers = {"Authorization": "Bot " + KAGI_API_KEY}
parameters = {"url": contents_url}

r = requests.get(api_url, headers=headers, params=parameters)
# print(r)

# print(r.json())

summary = r.json()['data']['output']

shorten_summary = textwrap.shorten(summary, width=150, placeholder=' [...이하 생략...]')
print("- 요약 내용(축약) : ", shorten_summary)