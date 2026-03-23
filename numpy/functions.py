import numpy as np

a=np.arange(1,11,1)                                             #list
b=np.arange(1,13,1).reshape(3,4)
g=np.array([[[1,2],[3,4]],[[4,9],[3,2]]])

print(a)
print(b)

c=np.ones((3,4))                         # simlarly np.zeros
d=np.linspace(-5,5,25)                      #inearly spaced numbers from -5 to 5
e=np.random.random((3,5))                   #random number matrix
f=np.identity(8)                            #identity matrix

print(c)
print(d)
print(e)
print(f)
print(g)

print(g.ndim)                                       # dimension of array 
print(g.shape)                                      # how many 2d rays are present,now of rows of 2d array, no of columns of 2d array
print(g.size)                                       # no of items in the array
print(g.itemsize)                                   # 

#  CHANGING DATATYPE
a.astype(np.int32)