import requests
from requests.auth import HTTPBasicAuth
import os
import json


data = open(r"param\param.json", "r")
data = json.load(data)

url = data['main_url']
api_key = data['main_key']
payload_limit = data['payload_limit']
speed_rate = data['speed_rate']
voice = data['voice']
cheerful = data['cheerful']
encoding = data['encoding']
headers = {
    "Content-Type": "application/json",
    "Accept": "audio/wav",
}

path_in = r'books'
path_out = r"audio"

if not os.path.exists(path_in):
    os.makedirs(path_in)
if not os.path.exists(path_out):
    os.makedirs(path_out)

for file_name in os.listdir(path_in):
    cpath_file_in = os.path.join(path_in, file_name)
    title = os.path.basename(cpath_file_in).replace(".txt","")
    with open(
        cpath_file_in,
        "r",
        encoding=encoding,
    ) as arquivo:
        content_data = arquivo.read()

    parts = [content_data[i : i + payload_limit] for i in range(0, len(content_data), payload_limit)]

    for i, part in enumerate(parts, start=1):
        data = {
            "text": part,
            "voice": voice, 
            "rate": speed_rate,
            "effects": {
            "cheerful": cheerful 
    }
        }
        
        response = requests.post(
            url,
            headers=headers,
            auth=HTTPBasicAuth("apikey", api_key),
            json=data,
        )

        if response.status_code == 200:
            with open(f"{path_out}/{title}-{i}.wav", "wb") as audio_file:
                audio_file.write(response.content)
            print(f"Part {i} from '{title}-{i}.wav'.")
        else:
            print(f"Erro on {i}: {response.status_code}")
            print(response.text)
