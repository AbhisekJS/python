from threading import*
from time import *

class bookmybus:
    def __init__(self,availableseats):
        self.availableseats=availableseats
        self.l=Lock()
    def buy(self, seatsrequested):
        self.l.acquire()
        if(self.availableseats>=seatsrequested):
            sleep(1)
            print("confirming a seat")
            print("processing Payment")
            print("printing your ticket")
            self.availableseats-=seatsrequested
            
            print("total seats available :",self.availableseats)
        else:
            print("Sorry, No seats available")
        self.l.release()

obj=bookmybus(15)
t1=Thread(target=obj.buy,args=(3,))
t2=Thread(target=obj.buy,args=(4,))
t3=Thread(target=obj.buy,args=(5,))
t1.start()
t2.start()
t3.start()