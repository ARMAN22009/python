import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,4,9,16,25,36,49,64,81,100,121,144,169,196])
y=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14])

u=np.linspace(-20,20,200)
v=u**2
k=np.sin(u)

plt.plot(u,k)
plt.show()

plt.plot(u,v)
plt.show()

