import numpy as np

# broadcasting  makes two arrays  have the same dimensions

# the smaller array is broadcasted across the larger array so that they have compatible shape

a=np.arange(6).reshape(2,3)
b=np.arange(3).reshape(1,3)
c=np.arange(3).reshape(3,1)

print(a)
print(b)
print(c)
print(a+b)


print(b+c)  
#  BROADCASTING RULES
#  make dimensions of both matrix same by adding a 1 at start
#  strecth the elements by multiplying 1 with the acceptable element


#  matrix b and c are broadcasted to form a compatible shape

# 0 1 2          0 0 0     0 1 2
# 0 1 2    +     1 1 1  =  1 2 3 
# 0 1 2          2 2 2     2 3 4



#(3x1)  and (1x3)    changed to (3x3) and (3x3)


# cannot be broadcasted together  as dimensions are not compatible
c= np.arange(12).reshape(3,4)
d= np.arange(12).reshape(4,3)

print(c)
print(d)
# print(c + d)                 # cannot be broadcasted

e= np.arange(12).reshape(3,4)
f=np.arange(3).reshape(3,1)
# f=np.arange(3).reshape(3)             # will not be compatible to add with e


print(e)
print(f)
print(e+f)                   # cannot be broadcasted