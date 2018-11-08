from flask import Flask
from flask import render_template, url_for, redirect, request, jsonify
import requests
import json
import time
import datetime

app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base,Day

engine = create_engine('sqlite:///days.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/', methods=['GET','POST'])
def newday():
    return render_template('index.html')


@app.route('/index', methods=['GET','POST'])
def data():
    daycount = session.query(Day).count()
    days = session.query(Day).all()
    return render_template('newfile.html', daycount = daycount, days = days)


@app.route('/file/<file_name>', methods=['GET','POST'])
def filename(file_name):
    headers = {
        'Authorization': 'Bearer 01M_lVdLpTBXgCcW3PtIAXASKjrS7wx4tUrLCV2WXW10DvjzP16l0dnRLziUTMbc1hL5qBJvhePqCZHZiRveKx07DWJ2w',
        'Content-Type': 'application/json',
    }
    print file_name

    # submit audio file
    data = '{"media_url":"http://www.wavsource.com/snds_2018-06-03_5106726768923853/people/famous/king_injustice.wav","metadata":"This is a sample submit jobs option"}' 
    # data = '{"media_url":"{}","metadata":"This is a sample submit jobs option"}'.format(file_name)
    response = requests.post('https://api.rev.ai/revspeech/v1beta/jobs', headers=headers, data=data).json()
    print ("got the id", response['id'])

    # check if audo file is done being transcribed
    jobId = response['id']
    headers = {
        'Authorization': 'Bearer 01M_lVdLpTBXgCcW3PtIAXASKjrS7wx4tUrLCV2WXW10DvjzP16l0dnRLziUTMbc1hL5qBJvhePqCZHZiRveKx07DWJ2w',
    }
    while (response['status'] != 'transcribed'):
        response = requests.get('https://api.rev.ai/revspeech/v1beta/jobs/'+ jobId, headers=headers).json()
        print (response['status'])
        time.sleep(0.1)

    # gets audio file text after done being transcribed
    headers = {
        'Authorization': 'Bearer 01M_lVdLpTBXgCcW3PtIAXASKjrS7wx4tUrLCV2WXW10DvjzP16l0dnRLziUTMbc1hL5qBJvhePqCZHZiRveKx07DWJ2w',
        'Accept': 'text/plain',
    }
    response = requests.get('https://api.rev.ai/revspeech/v1beta/jobs/'+ jobId +'/transcript', headers=headers)
    # get date of transcribe
    date = datetime.datetime.now().strftime("%A, %d %B %Y %I:%M%p")

    # create database query
    file = Day(date=date, href=file_name,
                text=response.text)
    session.add(file)
    session.commit()
    daycount = session.query(Day).count()
    return redirect(url_for('data'))

@app.route('/all')
def json():
    days = session.query(Day).all()
    return jsonify(Day=[i.serialize for i in days])

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
