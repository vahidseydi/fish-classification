from flask import Flask, request

application = Flask(__name__)

@application.route('/')
def test():
    return 'start'

