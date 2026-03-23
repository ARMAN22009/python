import numpy as np
a= np.array([1,0,3],dtype=np.int64)                                                                # vector
b=np.array([[1,2,3],[4,5,6]],dtype=float)                                                       # matrix
c=np.array([[[123],[223],[445]],[[123],[223],[445]],[[123],[223],[445]]],dtype=complex)           # tensor

print(a)
print(type(a))

print(b)
print(type(b))

print(c)
print(type(c))

print(c.ndim)
print(c.shape)
print(a.itemsize)                           #float=8, comlex=16, int=8 ,int32=4 ,int64=8
print(c.itemsize)