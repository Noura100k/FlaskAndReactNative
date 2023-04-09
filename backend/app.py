
from flask import Flask, Response, request, jsonify
from io import BytesIO
import base64
from flask_cors import CORS, cross_origin
import os
import sys
from PIL import Image 
import base64

app = Flask(__name__)
cors = CORS(app)

@app.route("/classify", methods=['POST'])
def image():
    if(request.method == "POST"):
        bytesOfImage = request.get_data()
        print(bytesOfImage)
        return "Image read"
      


        
        


