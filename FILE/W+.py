f=open("w+file.txt","w+")
data= f.write("i am not in danger i am the danger.")

# w+ truncates. it means it gets completely wiped out

print(f.read())
f.close()