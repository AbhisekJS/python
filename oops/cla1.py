class Mobile:
    def __init__(self,name,version,price):
        self.name=name
        self.version=version
        self.price=price
    
    def brand(self):
        print(self.name)
        print(self.version)
        print(self.price)

    def disount(self):
        dis=self.price*0.9
        return dis
    
    def tax(self):
        GST= self.price*.25
        return GST

c1=Mobile("oppo","A5",14000)
c2=Mobile("Apple","X",80000)
print (c1.name,c1.version, c1.price, c1.disount(),c1.tax())
print (c2.name,c2.version, c2.price, c2.disount(),c2.tax())
c2.tax()