from flask import Flask, jsonify, request, json
from flask_script import Manager

# from flask_cors import CORS, cross_origin

import speech
import vision

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

@app.route('/')
def index():
    return "<h1> I LOVE YOU </h1>"

#TODO: Take image in format
@app.route('/api/v1/image', methods=['POST'])
def image():
    img = Image.open(request.files['file'])
    return "HELLO"

app.run()
