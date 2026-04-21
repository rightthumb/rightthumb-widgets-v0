import schedule
import time
import os

def scheduler_job(args):
    print('RAN:', args)
    os.system(args)

def scheduler():
    schedule.every(5).seconds.do(scheduler_job, 'echo Hello, World!')  # Replace with your command
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    scheduler()