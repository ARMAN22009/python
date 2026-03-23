f=open("name.txt","w")
data = f.write("golu molu tolu")
# data will be overwritten from |rakesh mukesh suresh| to |golu molu tolu|


print(data)


l=["hello\n","good morning\n","manoj"]
f=open("C:\Podcasts\python\FILE\docu.txt","w")
k=f.writelines(l)

f.close()
print(k)