class Estudiante:

    def __init__(self,name,phy,math,chem):
        self.name=name
        self.m1=phy
        self.m2=math
        self.m3=chem

    def average(self): # self should be written
        avg=(self.m1+self.m2+self.m3)/3
        print(self.name,"you average score is :",avg)
        
e1=Estudiante("som",55,70,90)
e2=Estudiante("mannu",77,90,98)

print(e1.average())
print(e1.name,e1.m1)

l=[e1,e2]
print(l)
# [<__main__.Estudiante object at 0x000001B342CD6BA0>, <__main__.Estudiante object at 0x000001B342F64A50>]
# object adress is stored

for i in l:
    print(i.name,i.m1,i.m2,i.m3)        