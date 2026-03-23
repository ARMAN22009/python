f=open("name.txt","a")

data= f.write("\nraju kaju maju")

# append me bs upr me a likhte hai baki write likhte hai
# each time you run gthe code it will be printed

f.close()

# if file is not present then it can also be made by just opening it in append or write mode

# but if you want to open a file without vanishing  the present line of code ,then copy the path of the code and write in append mode.

f=open(r"C:\Podcasts\python\FILE\docu.txt","a")
dataa=f.write("\nmanu sala ")
f.close()