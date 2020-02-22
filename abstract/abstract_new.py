from abc import abstractmethod,ABC
class Mobile(ABC):
    def __init__(self,brand,price,feature):
        self.brand=brand
        self.price=price
        self.feature=feature

    @abstractmethod
    def network(self):
        pass
    
    @abstractmethod
    def bluetooth(self):
        pass

class smartphones(Mobile):
    def __init__(self,brand,price,feature,waranty):
        super().__init__(brand,price,feature)
        self.waranty=waranty

    def display(self):

        print(self.waranty)

    def network(self):
        super().network()
        print('4G Volte')
    
    def bluetooth(self):
        super().bluetooth()
        print('Bluetooth V 5.0')

phones=smartphones("MI",12000,"Android",True)
phones.display()
phones.bluetooth()
phones.network()
print(phones.brand,phones.price,phones.feature)
    

