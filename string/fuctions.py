str="me ,me and me alone , good"
print(str.endswith(" out"))
# true

print(str.capitalize())
str=(str.capitalize())
print(str.capitalize())

print(str.replace( "me" ,"him"))
print(str.replace("g","G"))

print(str.find("me"))
print(str.find("to"))
# -1 me not present

print(str.count("me"))
