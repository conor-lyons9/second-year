from multiprocessing import *

def sayHi():
    print("Hi from process", current_process().pid)

def procEx():
    print("Hi from process", current_process().pid, "(parent process)")

    otherProc = Process(target=sayHi, args=())

    otherProc.start()


# Creating multiple child processea
def procEx2():
    print("Hi from process", current_process().pid, "(parent process)")

    p1 = Process(target=sayHi, args=())
    p2 = Process(target=sayHi, args=())
    p3 = Process(target=sayHi, args=())

    p1.start()
    p2.start()
    p3.start()


def sayHi2(n):
    print("Hi", n, "from process", current_process().pid)

def manyGreetings():
    print("Hi from process", current_process().pid, "(main process)")

    name = "Jimmy"
    p1 = Process(target=sayHi2, args=(name,))
    p2 = Process(target=sayHi2, args=(name,))
    p3 = Process(target=sayHi2, args=(name,))

    p1.start()
    p2.start()
    p3.start()

#
def askName():
    name = input("What is your name?")
    numProc = int(input("How many processes do you want?"))
    
    for i in range(0, numProc):
        p = Process(target=sayHi2, args=(name,))
        p.start()

#####

def sayHi3(personName):
    for i in range(0,100000):
        j = i+10
    print("Hi", personName, "from process", current_process().name, "- pid", current_process().pid)

def manyGreetings3():
    print("Hi from process", current_process().pid, "(parent process)")

    personName = "Jimmy"
    for i in range(10):
        Process(target=sayHi3, args=(personName,), name=str(i)).start()

#

def sayHi4(lock, name):
    lock.acquire()
    print("Hi", name, "from process", current_process().pid)
    lock.release()

def manyGreetings4():
    lock1 = Lock()

    print("Hi from process", current_process().pid, "(main process)")

    for i in range(10):
        Process(target=sayHi4, args=(lock1, "p"+str(i))).start()

#
def worker(lock, name, hole):
    lock.acquire()
    print(f"Hiddy-ho!  I'm worker {name} and today I have to dig hole {hole}")
    lock.release()

def assignDiggers():
    lock2 = Lock()
    
    letters = ["A", "B", "C"]
    for i in range(3):
        Process(target=worker, args=(lock2, letters[i], i)).start()

assignDiggers()
