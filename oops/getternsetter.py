class corporate:

    def setName(self,n):
        self.name=n

    def getName(self):
        return self.name

    def setSalary(self,s):
        self.salary=s

    def getSalary(self):
        return self.salary

    def setTechnologies(self,techs):
        self.technologies=techs

    def getTechnologies(self):
        return self.technologies

c1= corporate()
c1.setName("Abhi")
c1.setSalary(5000)
c1.setTechnologies(["java","hibernate","string"])

print(' Created Info : {} - {}',format(c1.name,c1.technologies))
