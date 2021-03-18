from flask import Flask, request

application = Flask(__name__)

@application.route('/')
def test():
    return 'start'

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()

