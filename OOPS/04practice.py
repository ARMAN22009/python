# class A:

#     def m1(self):
#         return 20
    
# class B(A):

#     def m1(self):
#         return 30
    
#     def m2(self):
#         return 40
    
# class C(B):

#     def m2(self):
#         return 50
    
# object1=A()
# object2=B()
# object3=C()

# print(object1.m1())
# print(object2.m1())
# print(object3.m1())
# # 20
# 30
# 30


class A:
    def m1(self):
        return 20
    
class B(A):
    def m1(self):
        val=super().m1()+ 30
        return val
    
class C(B):
    def m1(self):
        val=self.m1()+ 20
        return val
    
object1=C()
print(object1.m1())

# object oc will call self in class c again and angan which will run an infinite loop and throw error