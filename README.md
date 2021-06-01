##example2不能运行，似乎是官网上flask_socketio的原始例子，目前还不知道怎么运行与调试

##example3可以正常使用，是类似微信聊天界面：
(1) app_chatbot.py
1.在浏览器中输入地址localhost:5000
2.在弹出的对话框中进行对话即可

(2)app_new正常运行
1.在浏览器中输入地址localhost:5000
2.定时显示数字

(3)app_new_apschedule.py在app_new正常运行基础上修改
可正常运行，使用了原始的apschedule来执行定时任务
(4)app_new_flask_apschedule.py在app_new正常运行基础上修改
可正常运行，使用了原始的apschedule结合flask-apschedule来执行定时任务



##example4不能运行，应该是在3基础上想进行改进的，但是还没有调试以及改进

Flask-SocketIO
==============

[![Build Status](https://travis-ci.org/miguelgrinberg/Flask-SocketIO.png?branch=master)](https://travis-ci.org/miguelgrinberg/Flask-SocketIO)

Socket.IO integration for Flask applications.

Installation
------------

You can install this package as usual with pip:

    pip install flask-socketio

Example
-------

```py
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('my event')
def test_message(message):
    emit('my response', {'data': 'got it!'})

if __name__ == '__main__':
    socketio.run(app)
```

Resources
---------

- [Tutorial](http://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent)
- [Documentation](http://flask-socketio.readthedocs.io/en/latest/)
- [PyPI](https://pypi.python.org/pypi/Flask-SocketIO)

