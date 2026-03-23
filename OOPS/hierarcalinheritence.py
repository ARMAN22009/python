class Phone:

    def __init__(self,company,model,price):
        self.company=company
        self.model=model
        self.price=price

    def buy(self):
        print(self.company,self.model," of price",self.price,"buying this phone")
        
        
class Smartphone(Phone):
    pass

class Featurephone(Phone):
    pass

s=Smartphone("samsung","s23","50000")
s.buy()