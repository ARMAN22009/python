import numpy as np

a1=np.arange(9)
a2=np.arange(1,13).reshape(3,4)
a3=np.arange(-1,26).reshape(3,3,3)

for i in a3[1,1,:]:
    print(i)

print(a3)
for i in np.nditer(a3):                                 # iteration for all the elements of any dimensional  array
    print(i)