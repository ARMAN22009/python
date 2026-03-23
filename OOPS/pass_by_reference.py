class Person:

    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

#outside class    creating a function

def greet(Person):                          # here object of a class is passed as an input to the function  
                                            #not evn object is passed here but the adress of object is passed 
    print("hello my name is ",Person.name,"and i am ",Person.gender)

p1=Person("Manoj","gay")
p2=Person("raka","male")

print(p1.name)                              # name is an INSTANCE VARIABLE,its value depends on objects ,like for objcet stored in p1 has value manoj  and for p2 raka
print(p2.name)