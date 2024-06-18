import openai
from IPython.display import Image, display

org_img_file = "./data/org_img_for_edit.png"
mask_img_file = "./data/mask_img_for_edit.png"

response = openai.Image.create_edit(
    image=open(org_img_file, "rb"),
    mask=open(mask_img_file, "rb"),
    prompt="YABAMOON who is criticing towards classmates in the classroom",
    n=1,
    size="512x512"
)

image_url = response['data'][0]['url']
print(image_url)
display(Image(url=image_url))
