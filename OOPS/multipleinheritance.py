# class Phone:

#     def __init__(self,name,model):
#         self.name=name
#         self.model=model

# class Product:

#     def review():
#         print("buying a phone")

# class smartphone(Phone,Product):

#     pass

# s=smartphone("samsung","s25")
# s.

class A:
    def action(self):
        print("A.action() called")
        super().action()

class B:
    def action(self):
        print("B.action() called")
        super().action()

class C(A, B):
    def action(self):
        print("C.action() called")
        super().action()

class D(C):
    def action(self):
        print("D.action() called")
        super().action()

class End:
    def action(self):
        print("End of chain")

# Change MRO to include End
class Final(D, End):
    pass

f = Final()
f.action()

# OUPTUP
# D.action() called
# C.action() called
# A.action() called
# B.action() called
# End of chain