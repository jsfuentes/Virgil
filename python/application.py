from flask import Flask, jsonify, request, json
from flask_script import Manager
from time import time

# from flask_cors import CORS, cross_origin

import speech
import vision

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

JVM_TOKEN = getNewJVMToken()
JVM_CREATION_TIME = time()

@app.route('/')
def index():
    return "<h1> I LOVE YOU </h1>"

#TODO: Take image in format
@app.route('/api/v1/image', methods=['POST'])
def image():
    # GET THE IMAGE FROM THE ARGUMENTS IN THE FORMAT
    img = "http://onpointfresh.com/wp-content/uploads/2016/03/95559ca9a79f7da23522cb702e5eb2e8.jpg"


    return "HELLO"

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()
