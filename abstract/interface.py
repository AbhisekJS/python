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
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass


class threeseries(bmw):

    def __init__(self,make,year,model,cruisecontrol):
        super().__init__(make,year,model)
        self.cruisecontrol=cruisecontrol

    def display(self):
        print(self.cruisecontrol)

    def start(self):
        super().start()
        print('ButtonStart')

    def stop(self):
        super().stop()
        print('ButtonStop')


    def drive(self):
        print("ThreeSeries is driven")


class fiveseries(bmw):

    def __init__(self,make,year,model,parkingassist):
        super().__init__(make,year,model)
        self.parkingassist=parkingassist

    def display(self):
        print(self.parkingassist)

    def drive(self):
        print("five series is driven")

    def start(self):
        super().start()
        print('ButtonStart')

    def stop(self):
        super().stop()
        print('ButtonStop')


ThreeSeries=threeseries("bmw",2009,"320i",True)
print(ThreeSeries.make)

print(ThreeSeries.model)
print(ThreeSeries.year)
print(ThreeSeries.cruisecontrol)
ThreeSeries.start()
ThreeSeries.display()
