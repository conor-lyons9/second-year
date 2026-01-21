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
    
    letters = ["A", "B", "C", "D", "E"]
    for i in range(len(letters)):
        Process(target=worker, args=(lock2, letters[i], i)).start()

#

import time

def greet2(q):
    for i in range(5):
        print("\n(child process) Waiting for name...")
        name = q.get()
        print("(child process) Well, hi", name)

def sendName2():
    q = Queue()

    p1 = Process(target=greet2, args=(q,))
    p1.start()

    names = ["Ciaran", "Sam", "Daniel", "AJ", "Sé"]
    for i in range(len(names)):
        time.sleep(1) # wait
        print("(parent process) Ok, I'll send the name")
        q.put(names[i])

#

def slowpoke(lock):
    time.sleep(2)
    lock.acquire()
    print("Slowpoke: Ok, I'm coming")
    lock.release()

def haveToWait():
    lock = Lock()
    p1 = Process(target=slowpoke, args=(lock,))
    p1.start()
    print("Waiter: Any day now...")

    p1.join()
    print("Waiter: Finally! Geez.")

#

def addTwoNumbers(a, b, q):
    time.sleep(2) # In case you want to slow things down to see what is happening.
    q.put(a+b)

def addTwoPar():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    q = Queue()
    p1 = Process(target=addTwoNumbers, args=(x, y, q))
    p1.start()

    print(q.get())

#

from multiprocessing import *
from random import randint
import time
def addManyNumbers(numNumbers, q):
    s = 0
    for i in range(numNumbers):
        s = s + randint(1, 100)
    q.put(s)

def addManyPar():
    totalNumNumbers = 1000000

    q = Queue()
    p1 = Process(target=addManyNumbers, args=(totalNumNumbers//2, q))
    p2 = Process(target=addManyNumbers, args=(totalNumNumbers//2, q))
    p1.start()
    p2.start()

    answerA = q.get()
    answerB = q.get()
    print("Sum:", answerA + answerB)

addManyPar()
