from threading import *
from time import sleep

class mythread:
    def displayn(self):
        i =0
        print(current_thread().getName())
        sleep(1)
        while (i<=10):
            print(i)
            i+=1
obj=mythread()
t1=Thread(target=obj.displayn)
t1.start()

t2=Thread(target=obj.displayn)
t2.start()

t3=Thread(target=obj.displayn)
t3.start()