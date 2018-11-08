from flask import Flask
from flask import render_template, url_for, redirect, request

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
    daycount = session.query(Day).count()
    return render_template('newfile.html', daycount = daycount)

@app.route('/file/<file_name>', methods=['GET','POST'])
def filename(file_name):

    # create database query
    file = Day(date="111111", href="linklink",
                text='text here')
    session.add(file)
    session.commit()
    daycount = session.query(Day).count()
    return redirect(url_for('newday'))



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
