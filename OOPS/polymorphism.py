#                                   # METHOD OVERRDING
# it happens when a parent and a child class both have method of same name , so on calling a method  using the object of child class the method of child class will be executed 

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):  #  Overriding the parent method
        print("Hello from Child")


obj=Parent()
obj.greet()     # hello from [parent]
objc=Child()
objc.greet()    # hello from [child]




#                                       METHOD OVER LOADING

# class Areacalc:

#     def area(self,radius):
#         self.radius=radius
#         print("inside 1")
#         ara=3.14*self.radius*self.radius
#         return ara
    
#     def area(self,l,b):
#         self.l=l
#         self.b=b
#         print("inside 2")
#         ara=self.l*self.b
#         return ara
    
# a1=Areacalc()
# a1.area(5,5)

# METHOD OVERLOADING -->> it is the case when in a class ,there are more than one method of same name is present  and they work based on the input provided
# makes the code more cleaner  rather than using areacirce arearectangle we only use area

                                        #WITHOUT USING METHOD OVERLOADING
# Now in python it is not supported but  we can use it also here 


class Area:
    def area(self,a,b=0):
        if (b==0):
            print(3.14*a*a)

        else :
            print(a*b)

a1=Area()
a1.area(2,4)
a1.area(2)
