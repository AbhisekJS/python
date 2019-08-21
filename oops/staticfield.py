class student:

    major='CSE'
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
s1=student("arvind",1)
s2=student("govind",2)
print(s1.major)
print(s2.major)
print(s1.name,s1.roll)
print(s2.name,s2.roll)
