class  Car:
    def __init__(self):
        self.model="SUV"

    @staticmethod                       #these are methods which will be inherited from the class car       
    def wheels():
        print("4 wheels")

    @staticmethod
    def seats():
        print("5 seats")

class BMW(Car):                                 #inheritence from PARENT CLASS (car)
    def __init__(self,name):
        self.name=name


b1=BMW("m3")
print(b1.name)
print(b1.model)

b1.seats()


# If child class  do not have any constructor then it accesses the parent class  constructor 
# If child class has its own constructor then parent class constructor will  not executed , so the variables inside the parent  constructor will not be initialized and cannot be accessed, if  we attemp to access it ,it will throw error