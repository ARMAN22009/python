a=float(input())
b=float(input())
c=float(input())
if (a>b):
    if(a>c):
        print("a is greater:",a)
    elif (c>a):
        print("c is greater:",c)

elif (a<b):
    if(b>c):
        print("b is greater:",b)
