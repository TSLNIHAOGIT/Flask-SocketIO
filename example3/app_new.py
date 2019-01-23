from gevent import monkey
monkey.patch_all()
from flask import Flask, render_template
from flask_socketio import SocketIO,emit
from threading import Lock
import random
async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
thread = None
thread_lock = Lock()

@app.route('/')
def index():
    # return render_template('test_new.html')#chatbot_original.html
    return render_template('test.html')#

@socketio.on('connect', namespace='/test_conn')
def try_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)

def background_thread():
    while True:
        socketio.sleep(1)
        t = random.randint(1, 100)
        socketio.emit('server_response',
                      {'data': t},namespace='/test_conn')

if __name__ == '__main__':
    socketio.run(app, debug=True)