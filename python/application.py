from flask import Flask, jsonify, request, json
from flask_script import Manager
from time import time
import cv2
import random

# from flask_cors import CORS, cross_origin

import speech
import vision
import screenshot
import deep_learning_object_detection_img

app = Flask(__name__)
# manager = Manager(app)
app.config['SECRET_KEY'] = 'hard to guess string'

JVM_TOKEN = speech.getNewJVMToken()
JVM_CREATION_TIME = time()

@app.route('/')
def index():
    print(JVM_CREATION_TIME)
    return "<marquee><h1 style='font-size:300px;'> I LOVE YOU </h1></marquee>"

@app.route('/audio', methods=['GET', 'POST'])
def audio():
    global JVM_CREATION_TIME
    global JVM_TOKEN
    # GET THE IMAGE FROM THE ARGUMENTS IN THE FORMAT
    img = "http://onpointfresh.com/wp-content/uploads/2016/03/95559ca9a79f7da23522cb702e5eb2e8.jpg"
    #JVM lasts for 10 minutes, so make sure its less than 8 minutes old
    if (time() - JVM_CREATION_TIME) > (8 * 60):
        JVM_TOKEN = speech.getNewJVMToken()
        JVM_CREATION_TIME = time()

    subject = vision.getSubjectByUrl(img)
    audio = speech.getAudioForText(subject, JVM_TOKEN)
    return audio

#TODO: Take image in format
@app.route('/api/v1/image', methods=['GET', 'POST'])
def image():
    global JVM_CREATION_TIME
    global JVM_TOKEN
    def imgToAudio(img, imgName, saveAudio=False, audioName="test.mp3"):
        cv2.imwrite(imgName, img)
        img = open(imgName, 'rb')
        subject = vision.getSubjectByImage(img)
        audio = speech.getAudioForText(subject, JVM_TOKEN)
        if saveAudio:
            f = open(audioName, 'wb')
            f.write(audio)
            f.close()
        return audio

    videoFile = request.data
    f = open("currentVideo.mov", 'wb')
    f.write(videoFile)
    f.close()

    imgs = screenshot.movToScreenshots("currentVideo.mov", 25, False)
    if len(imgs) == 0:
        print("No Img")
        motivationalInt = random.randint(0,4)
        f = open("../motivation" + str(motivationalInt) + ".mp3", 'r')
        audio = f.read()
        return audio

    cv2.imwrite("currentImage.jpg", imgs[0])
    if deep_learning_object_detection_img.colliding("currentImage.jpg", 1000):
        print("WATCH OUT")
        f = open("../STOP.mp3", 'r')
        audio = f.read()
        return audio

    #JVM lasts for 10 minutes, so make sure its less than 8 minutes old
    if (time() - JVM_CREATION_TIME) > (8 * 60):
        JVM_TOKEN = speech.getNewJVMToken()
        JVM_CREATION_TIME = time()

    # img = "http://onpointfresh.com/wp-content/uploads/2016/03/95559ca9a79f7da23522cb702e5eb2e8.jpg"
    # for img in imgs:
    imgToAudio(imgs[0], "img1.jpg", True, "audio1.mp3")
    audio = imgToAudio(imgs[-1], "img2.jpg", True, "audio2.mp3")
    return audio

# run the app.
if __name__ == "__main__":
    app.run()
