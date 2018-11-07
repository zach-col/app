from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/voiceupload/')
def voiceupload():
    # upload api and upload

    # send text saying its uploaded
    # redirect to state
    return render_template('voiceupload.html')


@app.route('/voiceupload/state/')
def voiceuploadstate():
    # get upload state
    # if state succes save
    # then redirect to all uploads
    return render_template('voiceuploadstate.html')

@app.route('/alluploads')
def allvoiceupload():
    return render_template('alluploads.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
