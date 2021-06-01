from gevent import monkey
monkey.patch_all()
from flask import Flask, render_template
from flask_socketio import SocketIO,emit
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler


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

@socketio.on('connect', namespace='/test_conn')#connect是固定的
def try_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)

def background_thread():

    # emit中的键与js代码socket.on中的键相对应
    t = random.randint(1, 100)
    socketio.emit('server_response1',  # 与js代码相对应，socket.on('server_response1', function(res) {
                  {'data': t}, namespace='/test_conn')


if __name__ == '__main__':
    scheduler = BackgroundScheduler(timezone="Asia/Shanghai")

    scheduler.add_job(background_thread, 'interval', max_instances=10, seconds=5)
    scheduler.start()

    socketio.run(app, debug=True)