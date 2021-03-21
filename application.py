from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
import io
import boto3
import logging
from botocore.exceptions import ClientError
# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer

from config import S3_BUCKET,S3_KEY,S3_SECRET



s3_resource = boto3.resource("s3",aws_access_key_id=S3_KEY,aws_secret_access_key=S3_SECRET)


# Define a flask app
application = Flask(__name__)
app = application
# Model saved with Keras model.save()
MODEL_PATH = 'models/model.h5'

# Load your trained model
#model = load_model(MODEL_PATH)
 #model._make_predict_function()          # Necessary
# print('Model loaded. Start serving...')



def model_predict(img_path, model):
    return ""
def get_result(response):
    s=[]
    s.append('Detected labels :' )
    s.append("\n")
    for label in response['Labels']:
        s.append ("Label: " + label['Name'])
        s.append("\n")
        s.append ("Confidence: " + str(label['Confidence']))
        s.append("\n")
        s.append ("Instances:")
        s.append("\n")
        for instance in label['Instances']:
            s.append ("  Bounding box")
            s.append("\n")
            s.append  ("    Top: " + str(instance['BoundingBox']['Top']))
            s.append("\n")
            s.append  ("    Left: " + str(instance['BoundingBox']['Left']))
            s.append("\n")
            s.append  ("    Width: " +  str(instance['BoundingBox']['Width']))
            s.append("\n")
            s.append  ("    Height: " +  str(instance['BoundingBox']['Height']))
            s.append("\n")
            s.append  ("  Confidence: " + str(instance['Confidence']))
            s.append("\n")

        s.append("\n")
        s.append("Parents:")
        for parent in label['Parents']:
            s.append("   " + parent['Name'])
        s.append ("----------")
        s.append("\n")
    return ''.join(s)


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to .s3/<bucetname>/test
       
        Key = 'test/{}'.format(secure_filename(f.filename))
        s3_resource.Bucket(S3_BUCKET).put_object(Key=Key,Body=f)
        
        # Make prediction
       
        '''
        client=boto3.client('rekognition','eu-west-2')
        response = client.detect_labels(Image={'S3Object':{'Bucket':S3_BUCKET,'Name':Key}},
        MaxLabels=10)
       

        print(str(len(response['Labels'])))
        result = get_result(response)               # Convert to string
        return result
        '''
        return "hello"
       

    return None


if __name__ == '__main__':
    # app.run(port=5002, debug=True)

    # Serve the app with gevent
    #http_server = WSGIServer(('', 5000), app)
    #http_server.serve_forever()
    app.debug=True
    app.run()
