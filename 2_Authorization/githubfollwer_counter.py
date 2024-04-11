import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--user", type=str, default="javadnematollahi")
opt = parser.parse_args()

url = f'https://api.github.com/users/{opt.user}'

response = requests.get(url=url)

followers = response.json()['followers_url']
following = response.json()['following_url'][0:-13]

response = requests.get(url=followers)
print(f'followers count is {len(response.json())}')

response = requests.get(url=following)
print(f'following count is {len(response.json())}')

