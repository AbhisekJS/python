from threading import *

def displayN():
    print(current_thread().getName())
    i=0
    while(i<=10):
        print(i)
        i+=1
print(current_thread().getName())
t=Thread(target=displayN)
t.start()