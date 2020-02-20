class car:

    def __init__(self,make,year):
        self.make=make
        self.year=year

    class engine():
        def __init__(self,engine):
            self.engine=engine
        def start(self):
            print("engines Started")

c=car("hector",2019)
#d=c.engine(1)
c.engine(1).start()
