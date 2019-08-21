from abc import abstractmethod,ABC

class maths(ABC):

    def __init__(self,num):
        self.num=num
        super().__init__()

    @abstractmethod
    def solve(self):
        pass

class add(maths):

    def solve(self):
        return self.num +"50"

x=add("50")
print(x.solve())
