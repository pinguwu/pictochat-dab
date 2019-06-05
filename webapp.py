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

url = 'mongodb+srv://{}:{}@{}/{}'.format(
    os.environ["MONGO_USERNAME"],
    os.environ["MONGO_PASSWORD"],
    os.environ["MONGO_HOST"],
    os.environ["MONGO_DBNAME"]
)
client = pymongo.MongoClient(os.environ["MONGO_HOST"])
db = client[os.environ["MONGO_DBNAME"]]
collection = db['messages'] #init

def setColl(collectionName):
    collection = db[collectionName]

def main():
    url = 'mongodb+srv://{}:{}@{}/{}'.format(
        os.environ["MONGO_USERNAME"],
        os.environ["MONGO_PASSWORD"],
        os.environ["MONGO_HOST"],
        os.environ["MONGO_DBNAME"]
    )
    client = pymongo.MongoClient(url)
    db = client[os.environ["MONGO_DBNAME"]]
    collection = db['DataB']

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/Chat1', methods=["GET", "POST"])
def renderchat1():

    allUserNames = "";
    #collection.find_one({})

    setColl("chat1")
    for text in collection.find({}):
        vrbl = str(text['_id'])
        allUserNames += "<p>" + text["user"] + ": " + text['message'] + "</p>" + '<form action = "/delete" method = "post"> <button type="submit" name="delete" value="'+vrbl+'">Delete</button> </form>'

    from bson.objectid import ObjectId
    return render_template('chat1.html', past_posts=Markup(allUserNames), async_mode = socketio.async_mode)

@app.route('/Chat2')
def renderchat2():
    return render_template('chat2.html', async_mode = socketio.async_mode)

@app.route('/Chat3')
def renderchat3():
    return render_template('chat3.html', async_mode = socketio.async_mode)

@app.route('/Chat4')
def renderchat4():
    return render_template('chat4.html', async_mode = socketio.async_mode)

@app.route('/posted', methods=["POST"])
def post():
    print("lol")
    post = {}
    print("lol1")
    post["user"] = "anon" #session['user_data']['login']
    print("lol2")
    post["message"] = request.form["message"]
    print("lol3")
    setColl(request.form["chatroom"])
    print("lol4")
    collection.insert_one(post)
    print("lol5")
    return redirect("/" + request.form["chatroom"])
        
def background_thread_1():
    pass



if __name__ == '__main__':
    socketio.run(app, debug=True)
