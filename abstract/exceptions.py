from abc import abstractmethod,ABC
class TouchScreenLaptop(ABC):


    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass


class HP(TouchScreenLaptop):


    def scroll(self):
        print("HP Notebook Scroll")

    def click(self):
        print("HP Notebook click")



class Dell(TouchScreenLaptop):


    def click(self):
        print("Dell Notebook Click")

    def scroll(self):
        print("Dell Notebook Scroll")

class HPNotebook(TouchScreenLaptop):

    def scroll(self):
        print("HP Notebook Scroll")

    def click(self):
        print("HP Notebook click")

class DellNotebook(TouchScreenLaptop):

    def click(self):
        print("Dell Notebook Click")

    def scroll(self):
        print("Dell Notebook Scroll")

dell=Dell()
print(dell.scroll())

hp=HP()
print(hp.scroll())

hpnote=HPNotebook()
print(hpnote.click())

dellnote=DellNotebook()
print(dellnote.click())
"""print(ThreeSeries.model)
print(ThreeSeries.year)
print(ThreeSeries.cruisecontrol)
ThreeSeries.start()
ThreeSeries.display()"""
