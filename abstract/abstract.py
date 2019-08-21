'''Abstract classes are classes that contain one or more abstract methods.
 An abstract method is a method that is declared, but contains no implementation.
 Abstract classes may not be instantiated,  and require subclasses to provide
 implementations for the abstract methods.
 Subclasses of an abstract class in Python are not required to implement abstract methods of the parent class.'''
from abc import abstractmethod,ABC
class bmw(ABC):
    def __init__(self,make,year,model):
        self.make=make
        self.year=year
        self.model=model

    def starthecar(self):
        print('starting the car')

    def stopthecar(self):
        print('stopping the car')

    @abstractmethod
    def drive(self):
        pass


class threeseries(bmw):

    def __init__(self,make,year,model,cruisecontrol):
        super().__init__(make,year,model)
        self.cruisecontrol=cruisecontrol

    def display(self):
        print(self.cruisecontrol)


    def drive(self):
        pass


class fiveseries(bmw):

    def __init__(self,make,year,model,parkingassist):
        super().__init__(make,year,model)
        self.parkingassist=parkingassist


    def drive(self):
        pass

ThreeSeries=threeseries("bmw",2009,"320i",True)
print(ThreeSeries.make)

print(ThreeSeries.model)
print(ThreeSeries.year)
print(ThreeSeries.cruisecontrol)
ThreeSeries.starthecar()
ThreeSeries.display()
