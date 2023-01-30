from multiprocessing import Process, current_process
import time

def worker():
    name = current_process().name
    print(name, 'Starting')
    time.sleep(2)
    print(name, 'Exiting')

def service():
    name = current_process().name
    print(name, 'Starting')
    time.sleep(3)
    print(name, 'Exiting')

if __name__ == '__main__':
    service = Process(name='Service 1', target=service)
    worker1 = Process(name='Worker 1', target=worker)
    worker2 = Process(name='Worker 2', target=worker)
    worker1.start()
    worker2.start()
    service.start()