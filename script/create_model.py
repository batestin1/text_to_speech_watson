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

custom_model = text_to_speech.create_custom_model(
    name='YodaSensei',
    language='en-GB',
    description='Translate, I can!'
).get_result()

file = open("param/custom_model.json", "w")
file.write(json.dumps(custom_model, indent=2))
