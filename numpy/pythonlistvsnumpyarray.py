import numpy as np

#  PYTHON LIST 

a=[i for i in range(10000000)]
b=[i for i in range(10000000,20000000)]

c=[]

import time
start=time.time()
for i in range(10000000):
    c.append(a[i]+b[i])
p=time.time()-start
print(p)


# NUMPY ARRAY

c=np.arange(10000000)
d=np.arange(10000000,20000000)
start=time.time()
x=c+d
q=time.time()-start
print(q)
 
print(p/q)

#    MEMORY USAGE BY PYTHON LIST VS   NUMPY ARRAY

import sys
print(sys.getsizeof(a))                            # python list
k=np.array(c,dtype=np.int32)
print(sys.getsizeof(k))                            # numpy array
