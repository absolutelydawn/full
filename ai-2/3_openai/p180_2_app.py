import openai
from IPython.display import Image, display
from pathlib import Path
import requests

dir_path = Path('./data')

dir_path.mkdir(parents=True, exist_ok=True)

response = openai.Image.create(
    prompt = "YABAMOON who claims towards classmates in the classroom",
    n = 2,
    size = "512x512"
)

for data in response['data']:
    image_url = data['url']

    image_filename = image_url.split("?")[0].split("/")[-1]
    image_path = dir_path / image_filename
    print("이미지 파일 경로 : ", image_path)

    r = requests.get(image_url)

    with open(image_path, 'wb') as f:
        f.write(r.content)
