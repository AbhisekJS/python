from abc import abstractmethod,ABC

class Touchscreenlaptop(ABC):

    def __init__(self,scroll,click):

        self.scroll=scroll

        self.click=click

class HP(Touchscreenlaptop):

    def scroll(self):

        super().scroll()

        print("scrolling")

class Dell(Touchscreenlaptop):

    def scroll(self):

        super().scroll()

        print("scrolling")





hpnotebook=HP("scroll button","click button")

dellnotebook=Dell("scroll button","click button")

print(hpnotebook.scroll)

print(hpnotebook.click)

print(dellnotebook.scroll)

print(dellnotebook.click)
