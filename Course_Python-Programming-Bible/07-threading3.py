#initiate a new thread

import threading
import time
import queue

exitFlag = 0

class BigThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q   #this will be more of a queue with priority queue
    def run(self):
        print("Starting: " + self.name)
        #threadLock.acquire()
        #TimeFunc(self.name, self.counter, 3)
        ProcessData(self.name, self.q)
        #print("Exiting ", self.name)
        threadLock.release()
        print("Exiting" + self.name)

def ProcessData(thread, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s" % (thread, data))

def TimeFunc(thread, delay, counter):
    while counter:
        #if exitFlag:
        #    thread.exit()
        time.sleep(delay)
        print("%s processing %s" % (thread, time.ctime(time.time())))
        counter -= 1

threadList = ["Thread 1", "Thread 2", "Thread 3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

for name in threadList:
    thread = BigThread(threadID, name, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

queueLock.acquire()

for word in nameList:
    workQueue.put(word)

queueLock.release()

while not workQueue.empty():
    pass

exitFlag = 1


for t in threads:
    t.join()

print("Exit the main thread")