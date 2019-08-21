class student:
    def __init__(self):
        self.__id=123
        self.__name="jhon"

    def display(self):
        print(self.__id)
        print(self.__name)

s = student()
e=s.display()

print(s._student__id, s._student__name);'''name mangling'''
