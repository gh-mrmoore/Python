#initiate a new thread

import threading
import time

class BigThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting: ", self.name)
        threadLock.acquire()
        TimeFunc(self.name, self.counter, 3)
        #print("Exiting ", self.name)
        threadLock.release()

def TimeFunc(thread, delay, counter):
    while counter:
        #if exitFlag:
        #    thread.exit()
        time.sleep(delay)
        print("%s: %s" % (thread, time.ctime(time.time())))
        counter -= 1

#try:
#    _thread.start_new_thread(TimeFunc("Thread Number 1", 1))
    #_thread.start_new_thread(TimeFunc("Thread Number 2", 2))
#except:
#    print("Some error...")

#while 1:
#    pass

threadLock = threading.Lock()
threads = []


thread1 = BigThread(1, "T1", 1)
thread2 = BigThread(2, "T2", 2)

thread1.start()
thread2.start()
#thread1.join()
#thread2.join()

threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()

print("Exit the main thread")