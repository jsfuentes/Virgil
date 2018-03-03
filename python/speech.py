import requests
from secret import SPEECH_API_KEY

#TODO: Only generate JVM Token when needed, maybe have two at a time
def getNewJVMToken():
    headers  = {'Ocp-Apim-Subscription-Key': SPEECH_API_KEY }

    #Need to generate JVM token that last for 10 minutes to make this request
    token_generator_url = "https://api.cognitive.microsoft.com/sts/v1.0/issueToken"
    response = requests.post(token_generator_url, headers=headers)
    JVM_token = response.text
    return JVM_token

def getAudioForText(text, JVM_token):
    speech_url = "https://speech.platform.bing.com/synthesize"

    headers = {
        'Ocp-Apim-Subscription-Key': SPEECH_API_KEY,
        'Authorization': "Bearer " + JVM_token,
        'Content-Type': "application/ssml+xml",
        'X-Microsoft-OutputFormat': 'audio-16khz-128kbitrate-mono-mp3',
        'User-Agent': 'Virgil', # I was told this was required
    }

    data = "<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-US'>" + \
        "<voice name='Microsoft Server Speech Text to Speech Voice (en-US, BenjaminRUS)'>" + \
        text + "</voice> </speak>" \

    response = requests.post(speech_url, headers=headers, data=data)
    audio = response.content
    return audio

if __name__ == "__main__":
    JVM_token = getNewJVMToken()
    text = "The big red dog jumped over the wall"
    audio = getAudioForText(text, JVM_token)
    f = open("sampleTest.mp3", 'wb')
    f.write(audio)
