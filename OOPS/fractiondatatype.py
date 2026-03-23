class Fraction:

    def __init__(self,x,y):
        self.num=x
        self.den=y
    
    def __str__(self):                   #magic method >>prints the return value when object is called to print
        return  "{}/{}".format(self.num,self.den)
    
    def __add__(self,other):             #gets triggered whever + is written inprogram  #self is taken as first number and other as second number
        num=self.num*other.den+self.den*other.num
        den=self.den*other.den
        return "{}/{}".format(num,den)
    
    def __sub__(self,other):
        num=self.num*other.den-self.den*other.num
        den=self.den*other.den
        return "{}/{}".format(num,den)
    
    def __mul__(self,other):
        num=self.num*other.num
        den=self.den*other.den
        return "{}/{}".format(num,den)
    
    def __truediv__(self,other):
        num=self.num*other.den
        den=self.den*other.num
        return "{}/{}".format(num,den)   #used to only write in fraction format avoiding division
    
    def covert_to_decimal(self):
        return self.num/self.den

f1=Fraction(3,5)
f2=Fraction(1,2)
print(f2.covert_to_decimal())

print(f1)
print(f1+f2)
print(f1-f2)
print(f1*f2)
print(f1/f2)
