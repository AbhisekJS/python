class objectcounter:
    noofobj =0
    def __init__(self):
        objectcounter.noofobj+=1

    @staticmethod
    def displaycount():
        print(objectcounter.noofobj)

o1= objectcounter()
o2= objectcounter()

objectcounter.displaycount()
