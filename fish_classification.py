from flask import Flask, request
import boto3

application = Flask(__name__)

@application.route('/')
def test():
    return 'start'

