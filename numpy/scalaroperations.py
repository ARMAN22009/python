import numpy as np

a=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

#   ARITMETIC OPERATORS

print(a+2)
print(a-2)
print(a*2)
print(a/2)
print(a**2)
print(a%2)
print(a)

# RELATIONAL OPERATORS

print(a >= 3)                        # comparision on each item of array
# [[[False False]
#   [False  True]]

#  [[ True  True]
#   [ True  True]]]