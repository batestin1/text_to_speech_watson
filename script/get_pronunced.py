import json
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

data = open(r"param\param.json", "r")
data = json.load(data)

url = data['main_url']
api_key = data['main_key']
payload_limit = data['payload_limit']
speed_rate = data['speed_rate']
voice = data['voice']
cheerful = data['cheerful']
encoding = data['encoding']
set_service_url = data['set_service_url']

authenticator = IAMAuthenticator(api_key)
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url(set_service_url)

pronunciation = text_to_speech.get_pronunciation(
    text='Hello dear, do you like comics books? I love Alan Moore!',
    voice='en-GB_KateVoice',
    format='ibm'
).get_result()
file = open("param/pronunciation.json", "w")
file.write(json.dumps(pronunciation, indent=2))
