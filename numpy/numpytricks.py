import numpy as np 

a=np.array([2,3,7,7,6666,733,82222])
b=np.random.randint(1,100,24).reshape(6,4)
print(np.sort(a))
print(np.sort(b,axis=0))    # column
print(np.sort(b,axis=1))    # row
print(np.sort(b))           # will do row wise sorting in such cases
print(np.sort(a)[::-1])     # descending sorting in 1d array

print(np.sort(b,axis=0)[::-1])          # column wise descend order


# APPEND

print(np.append(a,222222222))

print(np.append((b,np.zeros(b.shape[0],1)),axis=1))