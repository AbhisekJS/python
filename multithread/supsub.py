from threading import *

class mythread(Thread):
    def run(self):
        i = 0
        print(current_thread().getName())
        while (i<=10):
            print(i)
            i+=1
print(current_thread().getName())
t= mythread()
t.start()
