from multiprocessing import Process
import os
import time

def function1(x):
    x = pow(x,2) * 3 + x * 5 + 27
    time.sleep(0.1)

def function2(x):
    x = pow(x,2) * 6 + x - 100
    time.sleep(0.1)

processes = []
nr_of_processes = os.cpu_count()

#Creating processes:

for i in range(nr_of_processes):
    p1 = Process(target = function1)
    processes.append(p1)

for j in range(nr_of_processes):
    p2 = Process(target = function2)
    processes.append(p2)

for p1 in processes:
    p1.start()
    p1.join()

#or I could have started the second process.
