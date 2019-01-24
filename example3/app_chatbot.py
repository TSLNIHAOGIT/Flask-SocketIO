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
name_space='/test_conn'
def decode(msg):
    msg = re.sub(r'%u', r'\u', msg)
    msg = urllib.parse.unquote(msg)
    msg = msg.encode('latin-1').decode('unicode_escape')
    return msg

@app.route('/')
def index():
    # return render_template('test_new.html')#chatbot_original.html
    return render_template('chatbot_luo.html')#test.html


@socketio.on('connect', namespace=name_space)
def try_connect():

    ##while导致链接不上，发不出去消息
    # while True:
    #     socketio.sleep(5)

        # t = random_int_list(1, 100, 10)
        t='欢迎来到flask_socketio'

        #python代码中：emit的键与js的代码中socket.on中的键相对应，反之也是

        socketio.emit('server_response',#与socketio
                      {'data': t},
                      namespace=name_space)



#监听前端emit的client_send（js是前端代码，js中发送的也是前端消息；到服务器也就是后端。后端进行监听处理）
#后端监听前端，前端监听后端
@socketio.on('client_send',namespace=name_space)
def client_msg(msg):

    sentence = msg.get('data')
    sentence=decode(sentence)


    #发送emit('server_response'，让后端监听
    socketio.emit('server_response', {'data': sentence}, namespace=name_space)




if __name__ == '__main__':
    socketio.run(app, debug=True)