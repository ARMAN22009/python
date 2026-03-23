class   Dog:

    # def __init__(self,):
    __type="big"                     #private attribute

    def __name(self):                #private method
        print("chibaba")

    def  intro(self):               #private method or function can be called inside the class only 
        print("hi i am ")
        self.__name()           #method called
        print(  self.__type  )         #attribute called
        return
d1=Dog()

# print(d1.__type)
print(d1.intro())

d1.intro()