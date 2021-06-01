
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
import time,datetime
scheduler = BlockingScheduler(timezone="Asia/Shanghai")
# scheduler=BackgroundScheduler(timezone="Asia/Shanghai")
def logins():
    print('login in ')
    all_jobs=scheduler.get_jobs()
    #print()
    all_job_ids=[each.id for each in all_jobs]
    if '2' in all_job_ids:
        scheduler.remove_job('2')
    scheduler.add_job(func=job, id='2', trigger='interval', max_instances=5, seconds=3)



def get_data():
    print('crawer data')
    # scheduler.add_job(func=job, id='1', trigger='interval', max_instances=5, seconds=1)


from apscheduler.schedulers.blocking import BlockingScheduler

def job():
    print('job 3s')


if __name__=='__main__':

    # sched = BlockingScheduler(timezone='MST')
    # sched.add_job(job, 'interval', id='3_second_job', seconds=3)
    # sched.start()
    # scheduler = BackgroundScheduler(timezone="Asia/Shanghai")
    # scheduler = BlockingScheduler(timezone="Asia/Shanghai")
    scheduler.add_job(func=logins, id='1', trigger='interval', max_instances=5, seconds=60,next_run_time=datetime.datetime.now())

    scheduler.start()


    # while(True):
    #     print('main 1s')
    #     time.sleep(1)