import threading
import time

class ThreadCoundown(threading.Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True

    def run(self):
        print(self.name,'started')
        sec = 10
        while sec > 0:
            print(self.name,'countdown:',sec)
            sec -= 1
            time.sleep(1)
        print(self.name,'ended')

t1 = ThreadCoundown()
t2 = ThreadCoundown()

t1.start()
t2.start()

t1.join()
t2.join()