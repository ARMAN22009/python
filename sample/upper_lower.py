def count(x):
    upper=0
    lower=0

    for ch in x:
        if(ch.isupper()):
            upper=upper+1
        elif(ch.islower()):
            lower=lower+1

    print("uppercase",upper)
    print("lowercase",lower)

x=input("enter para:")  
count(x)
