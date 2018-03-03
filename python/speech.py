import requests
import pyglet

speech_api_key = '66acd4fff35c463a8a5053800bac79cf'
headers  = {'Ocp-Apim-Subscription-Key': speech_api_key }

#Need to generate JVM token that last for 10 minutes to make this request
token_generator_url = "https://api.cognitive.microsoft.com/sts/v1.0/issueToken"
response = requests.post(token_generator_url, headers=headers)
JVM_token = response.text

# Do it

speech_url = "https://speech.platform.bing.com/synthesize"
text = "Dog"

headers = {
    'Ocp-Apim-Subscription-Key': speech_api_key,
    'Authorization': "Bearer " + JVM_token,
    'Content-Type': "application/ssml+xml",
    'X-Microsoft-OutputFormat': 'audio-16khz-128kbitrate-mono-mp3', #this was a pseudo-randomly selected format
    'User-Agent': 'Virgil', # I was told this was required
}

data = "<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-US'>" + \
    "<voice name='Microsoft Server Speech Text to Speech Voice (en-US, BenjaminRUS)'>" + \
    text + "</voice> </speak>" \


response = requests.post(speech_url, headers=headers, data=data)
f = open("sampleTest.mp3", 'wb')
f.write(response.content)


# vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"
# vision_analyze_url = vision_base_url + "analyze"
# image_url = "http://onpointfresh.com/wp-content/uploads/2016/03/95559ca9a79f7da23522cb702e5eb2e8.jpg"
#
# headers  = {'Ocp-Apim-Subscription-Key': '0727313b6afe4e82ad687fbd28c98345' }
# params   = {'visualFeatures': 'Description,Tags,Faces'}
# data     = {'url': image_url}
# response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
# response.raise_for_status()
# analysis = response.json()
#
# print(analysis)
# image_caption = analysis["description"]["captions"][0]["text"].capitalize()
# print(image_caption)
