
from gevent import monkey
monkey.patch_all()
import requests

from requests.packages.urllib3.util.ssl_ import create_urllib3_context
create_urllib3_context()

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)