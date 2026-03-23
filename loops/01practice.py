numbers=[1,4,9,16,25,36,49,64,81,100,64]
indx=0
for num in numbers:
    if(num==64):
       print("number found  :",num)
       print("at index :",indx)
    indx+=1


even_odd = lambda x:"even" if x%2==0  else "odd"
print(even_odd(5))   # 