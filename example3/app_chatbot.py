from gevent import monkey
monkey.patch_all()
from flask import Flask, render_template
from flask_socketio import SocketIO,emit
from threading import Lock
import re

import pandas as pd
import numpy as np
import time
import requests
import urllib
import random
async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
thread = None
thread_lock = Lock()

def decode(msg):
    msg = re.sub(r'%u', r'\u', msg)
    msg = urllib.parse.unquote(msg)
    msg = msg.encode('latin-1').decode('unicode_escape')
    return msg

@app.route('/')
def index():
    # return render_template('test_new.html')#chatbot_original.html
    return render_template('chatbot_luo.html')#test.html


@socketio.on('connect', namespace='/test_conn')
def try_connect():

    ##while导致链接不上，发不出去消息
    # while True:
    #     socketio.sleep(5)

        # t = random_int_list(1, 100, 10)
        t='欢迎来到flask_socketio'
        socketio.emit('server_response',
                      {'data': t},
                      namespace='/test_conn')

@socketio.on('client_send',namespace='/test_conn')
def client_msg(msg):

    sentence = msg.get('data')
    sentence=decode(sentence)

    socketio.emit('server_response', {'data': sentence}, namespace='/test_conn')






if __name__ == '__main__':
    socketio.run(app, debug=True)