import numpy as np
# STACKING


a=np.array([[1,2],[4,5]])
b=np.array([[19,8,7],[88,7,5]])

print(np.hstack((a,a,b)))


print(np.vstack((a,a)))

# SPLITTING

a=np.array([[1,3,5],[3,6,9],[9,99,80]])

print(np.hsplit(a,3))               # horizontal split
print(np.vsplit(a,3))               # vertical split