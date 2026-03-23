
def printkarde(n):
    if (n!=0):
        
        print(n)
        printkarde(n-1)
    else:  return
    

print("enter n:")
n =int(input())

printkarde(n)



