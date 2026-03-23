import numpy as np

a=np.arange(9)
b=np.arange(1,13).reshape(3,4)
c=np.arange(27).reshape(3,3,3)

print(a)
print(a[-1])  # last element at index -1 and first  element at index 0

print(b)  
print(b[0,2])               # 0th row  and 2nd column

print(c)
print(c[0,1,2])

#   SLICING
#1D                                                                         
print(a[2:5])                                                             #  [2,3,4]
print(a[2:8:2])             # strides of 2                                 [2,4,6]

#2D
print(b)
print(b[0,:])               # first row  all elements 
print(b[:,3])               # 4th column elements 
print(b[:,:])               # all rows and all columns

print("_____________")
print(b[1:,1:4])            # 1st row onwards and columm 1 to  3 

print("_____________")
print(b[::2,::3])           # jump size in rows 1 ,jumps size in columns 2 

print("_____________")
print(b[:,::3])             # all of rows, jump size in coloumns is 3

print("_____________")
print(b[::2,1::2])            # 
print(b[1,::3])
print(b[0:2,1:4])

#3D
print(c)
print("             ")
print(c[1,1,1])
print("             ")
print(c[1,1:,1:])
print("             ")
print(c[0,1,:])
print("             ")
print(c[::2,0,::2])



# FANCY INDEXING

print( "FANCY INDEXING")
print(b[[0,2]])                                             # rows ,columns
print(b[:,[1,3]])