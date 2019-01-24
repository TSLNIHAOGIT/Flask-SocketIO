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


from flask import Flask
app=Flask(__name__)
from flask import  render_template,request
# from mong_database import MongoManager#这样子也可以
# from app.mong_database import MongoManager


from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import atexit
import time
import re
# mongo_db=MongoManager()

import urllib.request
from urllib.parse import quote
import pandas as pd
import numpy as np
import time
import re
name_space = '/chat'

def decode(msg):
    msg = re.sub(r'%u', r'\u', msg)
    msg = urllib.parse.unquote(msg)
    msg = msg.encode('latin-1').decode('unicode_escape')
    return msg

def get_data(sentence):
    #url中含有中文时要单独处理
    req = urllib.request.Request(
        'http://drea.cc/api/chat.php?msg={}&uid=drea_bbs_chat'.format(quote(sentence)))
    req.add_header('Content-type', 'text/xml; charset="gbk"')
    response = urllib.request.urlopen(req)
    buff = response.read()
    the_page = buff.decode('gbk')
    print(type(the_page),eval(the_page)['reply'])
    response.close()
    return eval(the_page)['reply']

'''/Users/ozintel/Downloads/Tsl_python_progect/local_ml/Flask-SocketIO/example4/app_run.py'''
#http://localhost:5000/
@app.route('/')#网页url的当前路径

#http://localhost:5000/index
@app.route('/')#网页url：/index为的当前路径
def index():
    return render_template(
                           # "index0.html",
                           "index_socket.html",
        async_mode=socketio.async_mode
                           )

@socketio.on('client_send', namespace=name_space)
def client_msg(msg):
    sentence = msg.get('data')
    sentence = decode(sentence)
    # sentences.append(sentence)
    print('sentence',sentence)
    response=sentence
    socketio.emit('my_response', {'data': response},room=1, namespace=name_space)




def disconnect_frontend(uid):
    socketio.emit('my_response',{'status':'disconnected'},room = uid, namespace=name_space)


@socketio.on('connect',namespace=name_space)
def connect():
    t = '欢迎来到flask_socketio'
    socketio.emit('my_response',
                  {'data': t},
                  room=1,
                  namespace=name_space)


# @app.route("/predict", methods= ["POST"])
# def background_process():
#     if request.method == 'POST':
#         try:
#             query = request.form.get('query')#前端查询的内容
#             if query:
#
#                     print('query',query)
#                     # time.sleep(5)
#                     result = get_data(query)
#                     print('result',result)
#                     #保存
#                     # mongo_db.save_query(query, str(result))
#                     return str(result)
#
#             else:
#
#                     return str('请输入查询内容')
#
#
#         except Exception as e:
#
#             if 'duplicate' in str(e):
#                 e_str = e.details['errmsg']
#                 dup_id=re.search('\{ : "(.*)" \}',e_str).group(1)
#                 print('重复查询同一句话,存储时使用相同的_id_',dup_id)
#                 # mongo_db.update_dup_query( dup_id, str(result))
#                 return str(result)
#
#             else:
#                 print(e)
#                 print('有问题，MM出故障啦')
#                 return str('MM出故障啦')
#
#         # finally:
#         #     # print(e)
#         #     print('有问题，MM出故障啦。。')
#         #     return str('MM出故障啦。。')
#
#     else:
#         return 'ok'

# @app.route('/dataFromAjax_post',methods=['POST','GET'])
# def dataFromAjax_post():
#     if request.method == 'POST':
#
#         try:
#             # query = request.form.get('mydata')  # 前端查询的内容
#             query = request.form['mydata']  # 前端查询的内容
#             if query:
#
#                 print('query', query)
#                 # time.sleep(5)
#                 result = '欢迎光临'
#                 print('result', result)
#                 # mongo_db.save_query(query, str(result))
#                 return str(result)
#             else:
#
#                 return str('请输入查询内容')
#         except Exception as e:
#             print('exception', e)
#             return str('有问题')
#     else:
#         return 'ok'



if __name__=='__main__':
    # scheduler = BackgroundScheduler()
    # scheduler.start()
    # scheduler.add_job(
    #     func=time.time,
    #     trigger=IntervalTrigger(seconds=3),
    #     id='purge_cache',
    #     name='purge_inactive',
    #     replace_existing=True)
    # # Shut down the scheduler when exiting the app
    # atexit.register(lambda: scheduler.shutdown())
    socketio.run(app, '0.0.0.0', port=5000,debug=True)
