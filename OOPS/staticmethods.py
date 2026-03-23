class Menu:

    def __init__(self,noodle,icecream)  :
        self.d1=noodle
        self.d2=icecream
    @staticmethod   #decorator
    def welcome():# method in which self parameter is not required is called a static method
        print("welcome")
 
lazeez=Menu("koreandhamaka","creamykulfi")

print(lazeez)
print(lazeez.d1,lazeez.d2)