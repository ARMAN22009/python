def factorial(n):
    fact = 1
    for number in range(1, n+1):
        fact=fact*number
    return fact  # return after the loop ends

n = int(input("Enter a number: "))

print("Factorial of the number is:", factorial(n))
