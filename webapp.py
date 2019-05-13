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

@app.route('/Chat1')
def renderchat1():
    
@app.route('/Chat2')
def renderchat2():
    
@app.route('/Chat3')
def renderchat3():
    
@app.route('/Chat4')
def renderchat4():
    
if __name__ == '__main__':
    socketio.run(app, debug=True)
