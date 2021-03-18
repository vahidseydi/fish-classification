from flask import Flask, request
import boto3

application = Flask(__name__)

@app.route('/')
def index():
    return '''<form method=POST enctype=multipart/form-data action="upload">
    <input type=file name=myfile>
    <input type=submit>
    </form>'''

@app.route('/upload', methods=['POST'])
def upload():
    s3 = boto3.resource('s3')
    s3.Bucket('coastal-images').put_object(Key='img1.jpg',Body=request.files['myfile'])
    return '<h1>File saved to S3</h1>'

if __name__ == '__main__' :
    app.run(debug=True)
