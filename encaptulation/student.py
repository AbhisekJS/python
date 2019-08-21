class student:

    def setId(self,id):
        self.id=id

    def getId(self):
        return self.id

    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

s= student()
s.setId(123)
s.setName("John")
print(s.id)
print(s.name)
print(s.getId())
print(s.getName())
