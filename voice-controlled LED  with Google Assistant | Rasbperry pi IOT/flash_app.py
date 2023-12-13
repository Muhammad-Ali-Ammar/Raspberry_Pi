
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import request

app = Flask(__name__)

Led = '0'



@app.route('/')
def root():
    return "root"



@app.route('/rpi')
def rpiFunction():
    global Led
    return Led


@app.route('/ifttt')
def iftttFunction():
    global Led
    Led = (request.get_data())
    return ''


