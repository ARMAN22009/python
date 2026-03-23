class  Car:
    
    @staticmethod
    def wheels():
        print("4 wheels")

    def seats():
        print("5 seats")

class  Brand(Car):

    def __init__(self,name):
        self.name=name

class  Model(Brand):

    def __init__(self,model):
        self.model=model
        return self.model


c1=Model("BMW","m5")


