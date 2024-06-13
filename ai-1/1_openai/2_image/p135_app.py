import openai

prompt = 'pretty anime girl'

response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="512x512"
)
image_url = response["data"][0]["url"]
print(image_url)

print(response)