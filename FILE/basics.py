f= open("docu.txt","r")

# read(5)  ---  only first five letters will be read
data = f.read(5)
print(data)
print(type(data))

                # OR
k=open("man.txt","r")

line1 = k.readlines()               # readlines reads all ines into a list,readline reads one lin
line2 = k.readlines()
print(line1)                        # print line changes line and readline also changes line so there will
print(line2)
print(type(line1))
# line1 will not be read because in start  entire file was read 
# so entire doc will be read only 


f.close()
# when file is created  it is stored in ROM but when it is opened it is shared in RAM the after making changes when we close the file then it is saved inside the ROM 

# cannot read after closing the file.
# print(f.read())


#   create multi line string

f=open("namesec.txt","w")
print(f.write("dolumanntu"))                                    # prints the number of characters
print(f.write("\nchampu hai kya?"))                             # prints the number of characters
f.close()

# if you are opening an existing file then the written lines on those file vanishes and the new pieces of lines are added .

