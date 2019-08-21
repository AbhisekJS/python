class data:
    def __init__(self,name,age,ratings):
        self.name=name
        self.age=age
        self.ratings=ratings

    def average(self):
        ''' defining an instance method'''
        noofratings=len(self.ratings)
        average=sum(self.ratings)/noofratings
        print("avg ratings ,", self.name, "is",average)

    def display(self):
        print(self.name)
        print(self.age)



c1= data("Abhi",28,[1,3,3,5,4])
print (c1.name)
c1.average()
c1.display()

c2= data("Tom",17,[1,5,3,4,2])
c2.average()
