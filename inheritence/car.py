class bmw:
    def __init__(self,make,year,model):
        self.make=make
        self.year=year
        self.model=model

    def starthecar(self):
        print('starting the car')

    def stopthecar(self):
        print('stopping the car')


class threeseries(bmw):

    def __init__(self,make,year,model,cruisecontrol):
        bmw.__init__(self,make,year,model)
        self.cruisecontrol=cruisecontrol

    def display(self):
        print(self.cruisecontrol)

class fiveseries(bmw):

    def __init__(self,make,year,model,parkingassist):
        bmw.__init__(self,make,year,model)
        self.parkingassist=parkingassist

ThreeSeries=threeseries("bmw",2009,"320i",True)
print(ThreeSeries.make)

print(ThreeSeries.model)
print(ThreeSeries.year)
print(ThreeSeries.cruisecontrol)
ThreeSeries.starthecar()
ThreeSeries.display()
