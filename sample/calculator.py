
def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Division by zero not allowed"
    return a / b

a=float(input("enter  first number :"))
b=float(input("enter seconnd mumber:"))



print("1.Add 2.Subtract 3.Multiply 4.Divide")
choice = int(input("Enter choice: "))

if choice == 1:
    print("Result =", sum(a, b))
elif choice == 2:
    print("Result =", sub(a, b))
elif choice == 3:
    print("Result =", mul(a, b))
elif choice == 4:
    print("Result =", div(a, b))
else:
    print("Invalid choice")