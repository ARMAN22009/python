import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[2,3],[4,5]])

#    VECTOR OPERATIONS

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(b**a)

#   max/min/sum/prod
print("max/min/sum/prod")

print(np.max(a))                                # maximum of all
print(np.max(a,axis=0))                         # maximum across each column (0)
                                                # 0--> column    1--> row
print(np.max(a,axis=1))                         # maximum across each  row   (1)

print(np.sum(a))
print(np.sum(a,axis=0))
print(np.sum(a,axis=1))

print(np.prod(a))

#  MEAN /MODE/ STD / VAR
print( "MEAN /MODE/ STD / VAR")

print(np.mean(b))
print(np.mean(b,axis=0))
print(np.mean(b,axis=1))

print(np.median(b))

print(np.std(b))

print(np.var(b))

print("TRIGNOMETRIC FUNCTION")

print(np.sin(b))

print("DOT PRODUCT")

u=np.arange(12).reshape(3,4)                                            # 3x4  multiplied by  4x3   gives  3x3 matrix
v=np.arange(12,24).reshape(4,3)
print(np.dot(u,v))
print(u,v)

print("LOG / EXPONENT")

print(np.exp(a))

print("round / floor / ceil")

k=np.array([[1.9,2.4],[3.5,44.99]])
print(np.round(k) )                             # round -->> round of the no to nearest integer
print(np.floor(k) )                            # floor -->> takes to the back integer   8.9-->8
print(np.ceil(k))                               #ceil-->> takes to the forward integer  8.1--> 9

print("transpose")

print(np.transpose(v))
print(v.T)

print("ravel")                                  # converts any dimensional array to 1D array

print(np.ravel(v))
print(v.ravel()) 