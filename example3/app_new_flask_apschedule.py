from gevent import monkey
monkey.patch_all()
from flask import Flask, render_template
from flask_socketio import SocketIO,emit
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from flask_apscheduler import APScheduler

from threading import Lock
import random
async_mode = True
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
    print('t={}'.format(t))
    socketio.emit('server_response1',  # 与js代码相对应，socket.on('server_response1', function(res) {
                  {'data': t}, namespace='/test_conn')
def background_thread_mew():

    # emit中的键与js代码socket.on中的键相对应
    t = random.randint(1, 100)
    print('new t={}'.format(t+3))
    socketio.emit('server_response1',  # 与js代码相对应，socket.on('server_response1', function(res) {
                  {'data': t+3}, namespace='/test_conn')
class Config:
    """App configuration."""

    JOBS = [
        {
            "id": "job1",
            "func": "app_new_flask_apschedule:background_thread",
            # "args": (1, 2),
            "trigger": "interval",
            "seconds": 3,
        }
    ]

    # SCHEDULER_JOBSTORES = {"default": SQLAlchemyJobStore(url="sqlite://")}
    #
    # SCHEDULER_EXECUTORS = {"default": {"type": "threadpool", "max_workers": 2}}
    #
    # SCHEDULER_JOB_DEFAULTS = {"coalesce": False, "max_instances": 3}

    # SCHEDULER_API_ENABLED = True


if __name__ == '__main__':
    ##通过配置文件的方式似乎还有点问题,可能必须是flask吧，这里是flask_socketio
    ##flask_socketio后面不在燕姐flask_apscheduler
    # app.config.from_object(Config())
    # scheduler = APScheduler()

    scheduler = BackgroundScheduler(timezone="Asia/Shanghai")
    scheduler = APScheduler(scheduler)
    scheduler.add_job(func=background_thread_mew, id='1',trigger='interval', max_instances=5, seconds=3)



    scheduler.init_app(app=app)
    scheduler.start()

    socketio.run(app, debug=True)