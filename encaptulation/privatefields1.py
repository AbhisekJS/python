class car:

    def Type(self,name,make,year):
        self.__name=name
        self.__make=make
        self.__year=year

    def display(self):
        print(self.__name)
        print(self.__make)
        print(self.__year)
    
s=car()
s.Type("320d","BMW",2002)
print(s._car__name);
print(s.display())