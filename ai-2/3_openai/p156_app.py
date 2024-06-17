import openai
import os

# API key set up
openai.api_key = os.environ["OPENAI_API_KEY"]

models = openai.Model.list()

# print(models["data"])
print(models["data"] [0] ["id"])