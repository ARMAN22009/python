
def factorial(n):
    fact=1
    for number in range(1,n+1):

        fact=fact*number
    return  fact

n=int(input())

print("factorial of the number is :",factorial(n))

# print(fact)