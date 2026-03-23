def summ(n):
    if (n==0) :
        return 0
    result = n +summ(n-1)
    return  result 
   
    


print("enter number :")
n = int(input())

summ(n)

print( result )

