import threading
import time
class CriticalSection:
    def _init_(self):
        self.sem = threading.Semaphore()
    def process1(self):
        while True:
            print('Entry section 1')
            self.sem.acquire()
            self.criticalsection()
            self.sem.release()
            print('Critical Section over for process1')
            time.sleep(3)
    def process2(self):
        while True:
            print('Entry section 2')
            self.sem.acquire()
            self.criticalsection()
            self.sem.release()
            print('Critical Section over for process2')
            time.sleep(3)
    def criticalsection(self):
        print('Entered the critical section, perform operation on shared resource')
if _name_ == '_main_':
    t1 = threading.Thread(target = CriticalSection().process1)
    t1.start()
    t2 = threading.Thread(target = CriticalSection().process2)
    t2.start()
