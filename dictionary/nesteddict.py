info = {
    "name":"Arman",
    "class":"10",
    "subjects":{
        "maths":"30",
        "chem":"69",
         }
}
print(info["subjects"]["maths"])
print(info)                                 

print(info.keys())
print(info["subjects"].keys())

print(list(info.keys()))
print(info.values())

print(info.items())
print(list(info.items()))
#  type casting it  into lists

pairs=list(info.items())

print(pairs[0])
print(pairs[2])

print(info["name"])
print(info.get("name"))