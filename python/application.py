from flask import Flask, jsonify, request, json
from flask_script import Manager
from time import time

# from flask_cors import CORS, cross_origin

import speech
import vision

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

JVM_TOKEN = speech.getNewJVMToken()
JVM_CREATION_TIME = time()

@app.route('/')
def index():
    print(JVM_CREATION_TIME)
    return "<marquee><h1 style='font-size:300px;'> I LOVE YOU </h1></marquee>"

#TODO: Take image in format
@app.route('/api/v1/image', methods=['POST'])
def image():
    global JVM_CREATION_TIME
    global JVM_TOKEN
    # GET THE IMAGE FROM THE ARGUMENTS IN THE FORMAT
    img = "http://onpointfresh.com/wp-content/uploads/2016/03/95559ca9a79f7da23522cb702e5eb2e8.jpg"
    #JVM lasts for 10 minutes, so make sure its less than 8 minutes old
    if (time() - JVM_CREATION_TIME) > (8 * 60):
        JVM_TOKEN = speech.getNewJVMToken()
        JVM_CREATION_TIME = time()

    subject = vision.getSubject(img)
    audio = speech.getAudioForText(subject, JVM_TOKEN)
    f = open("test_input.mp3", 'wb')
    f.write(audio)
    f.close()
    return audio

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run(port=4000)
