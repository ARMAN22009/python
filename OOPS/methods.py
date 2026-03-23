class Boy:

    def __init__(self,name):
        self.name=name

    def greet(self):  #method(a function made inside a class , which is made for objects)
        print("hello",self.name)
    
b1=Boy("raju")
print(b1.name)

b1.greet()  #hello raju