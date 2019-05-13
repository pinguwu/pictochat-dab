from flask_oauthlib.client import OAuth
from flask import render_template
from bson.objectid import ObjectId
from threading import Lock
from flask import Flask, redirect, url_for, session, request, jsonify, Markup, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect

import pymongo
import sys
import dns
import pprint
import os
#os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
app.debug = True
socketio = SocketIO(app, async_mode=None)
thread = None
thread_lock = Lock() 


@app.route('/')
def index():
    return render_template('home.html', async_mode=socketio.async_mode)

@app.route('/chat1')
def renderChat1():
    
@app.route('/chat2')
def renderChat2():
    
@app.route('/chat3')
def renderChat3():
    
@app.route('/chat4')
def renderChat4():
    
if __name__ == '__main__':
    socketio.run(app, debug=True)
