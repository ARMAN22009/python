n = int(input("Enter number of terms: "))

fib = [0, 1]

for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])

print("Fibonacci List:", fib)

# even_sum = sum(x for x in fib if x % 2 == 0)
# print("Sum of even terms:", even_sum)
fib_even=[]
if (fib[i]%2 ==0):
    fib_even.append(fib[i])

print(fib_even)