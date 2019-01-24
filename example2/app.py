from gevent import monkey
monkey.patch_all()

# monkey.patch_all()的导入要放在所有的前面
import requests



from flask import Flask
from flask_socketio import SocketIO,send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret!'
socketio = SocketIO(app)

@socketio.on('message')
def handleMessage(msg):
    print('message',msg)
    send(msg,broadcast=True)

if __name__ == '__main__':
    socketio.run(app)