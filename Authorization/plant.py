import argparse
import dotenv
import os
import requests
import shutil


parser = argparse.ArgumentParser()
parser.add_argument("--plant", type=str, default="ficus")
opt = parser.parse_args()


url = "https://fal.run/fal-ai/illusion-diffusion"
dotenv.load_dotenv()
illusion = os.getenv("illusion-diffusion")
headers = {
    "Authorization": f"Key {illusion}",
    "Content-Type": "application/json"
}

payload = {
    "image_url": "https://storage.googleapis.com/falserverless/illusion-examples/checkers.png",
    "prompt": f"(masterpiece:1.4), (best quality), (detailed),(just one plant with no extra flower or tree), {opt.plant}",
    "negative_prompt": "(worst quality, poor details:1.4), lowres, (artist name, signature, watermark:1.4), bad-artist-anime, bad_prompt_version2, bad-hands-5, ng_deepnegative_v1_75t"

}

response = requests.post(url, headers=headers, json=payload)
try:
    res=response.json()
except:
    print(f"https://fal.run/fal-ai/illusion-diffusion server response is {response.status_code}")


res = requests.get(res['image']['url'], stream = True)

if res.status_code == 200:
    with open('assets/image.jpg','wb') as f:
        shutil.copyfileobj(res.raw, f)
    print('Image sucessfully Downloaded: ','assets/image.jpg')



#####  Read image and give it to plant
    
url = "https://my-api.plantnet.org/v2/identify/all"
dotenv.load_dotenv()
plant = os.getenv("plant")
headers = {}
payload = {
    "api-key": f"{plant}"
}
files = {
    "images": open("assets/image.jpg", "rb")
}
try:
    response = requests.post(url, headers=headers, params=payload, files=files)
    print(response.json()['bestMatch'])
except:
    print(f"https://my-api.plantnet.org server response is {response.status_code}")
