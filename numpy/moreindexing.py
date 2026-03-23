import numpy as np

a=np.arange(1,28).reshape(3,9)
b=np.random.randint(1,101,25).reshape(5,5)

print(a)
print(b)

# BOOLEAN INDEXING

print(a>23)
print(a[a>23])                    # find only number which are more than 23
print(a[(a%2==0) & (a>5)])        # find numbers which are divisibe by 2 as well as they are even numbers
print(a[~(a%7==0)])               # not operator