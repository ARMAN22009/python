f= open("boy.txt","r+")
data= f.write("\n10 years old.")

print(data)
# print(f.write())
print(f.read())
f.close()

# it will overwrite the pevious data in the file
#                       OUTPUT
# 14
# ---taplu don maja