from threading import Thread, Lock, current_thread
from queue import Queue
import time

def basic_function(q, l):
    while True:
        val=q.get()
        with l:
            print(f"{current_thread().name}-->{val}")
        q.task_done()

if __name__ == "__main__":

    l = Lock()
    q = Queue()
    n = 5 #num of threads

    for i in range(n):
        t = Thread(target=basic_function, args=(q,l))
        t.daemon=True
        t.start()

    for j in range(1,11):
        q.put(j)

    q.join()
