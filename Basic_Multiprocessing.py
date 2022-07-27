from multiprocessing import Process, Array, Lock, Value, Queue
import time

def function1_add2(Arr,q):
    for n in Arr:
        q.put(n+1)

def function2_divdeby2(Arr,q):
    for n in Arr:
        q.put(n/2)

if __name__ == "__main__":

    q = Queue()
    Arr = Array("i", [0,100,200])

    P1 = Process(target=function1_add2(Arr, q))
    P2 = Process(target=function2_divdeby2(Arr, q))

    P1.start()
    P2.start()

    P1.join()
    P2.join()

    while not q.empty():
        print(q.get())
