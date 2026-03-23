import numpy as np  
import pandas as pd  

name=["kala","manu","jabal"]
print(pd.Series(name))
f=pd.Series(name)

# CUSTOM INDEXING

# NAME setting

marks=[23,44,56]
print(pd.Series(marks,index=name, name= "bachoo ke marks"))          # index will be replaced here by names

# serie from dictionary

marks={
    "maths": 55,                        # keys index ban jate hai aur values 
    "chem": 77,
    "physics": 98,
}
k=pd.Series(marks,name="arman ke marks")
print(k)

print(k.size)
print(k.dtype)
print(k.name)
print(k.is_unique)                                          # if items are unique or not

rollno=pd.Series([1,2,3,4,5,6,7,8,9])
print(rollno.is_unique)
print(k.index)                                              # index

print(k.values)                                             # gives an array
