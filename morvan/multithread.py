import threading
import time
from queue import Queue

def thread_job():
    print('T1 start \n')
    for i in range(10):
        time.sleep(0.1)
    print('T1 finish \n')

def T2_job():
    print('T2 start \n')
    print('T2 finish \n')

def job(l):
   for i in range(len(l)):
      pass元组

def multithreading(data):

def main():
    added_thread = threading.Thread(target=thread_job,name='T1')
    thread2 = threading.Thread(target=T2_job,name='T2')
    added_thread.start()
    thread2.start()
    thread2.join()
    added_thread.join()

    print('all done \n')


if __name__ == '__main__':
    main()