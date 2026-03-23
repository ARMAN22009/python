class Person:
    def __init__(self):
        self.name="habibi"
       
Person()                            # yes,here the object is created 


p1=Person()                         # we  assume p1 is an object of Person calss ,but it is not , rather by just calling Person()  object is created .
                                   # now the object that is created by calling Person() is stored in p1 as reference(adress) of the object created.
                                   # and that is  why p1 is called as reference variable

q1=p1                               #now q1 is storing the 
print(p1.name)
print(q1.name)
q1.name="mulla"                     #
print(q1.name)
print(p1.name)
