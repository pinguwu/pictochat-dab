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

chat1_data = {}
chat2_data = {}
chat3_data = {}
chat4_data = {}


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/Chat1')
def renderchat1():
    return render_template('chat1.html', async_mode = socketio.async_mode)

@app.route('/Chat2')
def renderchat2():
    return render_template('chat2.html', async_mode = socketio.async_mode)

@app.route('/Chat3')
def renderchat3():
    return render_template('chat3.html', async_mode = socketio.async_mode)

@app.route('/Chat4')
def renderchat4():
    return render_template('chat4.html', async_mode = socketio.async_mode)

def background_thread_1():
    pass

def background_thread_2():
    pass

def background_thread_3():
    pass

def background_thread_4():
    pass


if __name__ == '__main__':
    socketio.run(app, debug=True)
