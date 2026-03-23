biodata={
    "name":"Mohammad Arman",
    "age": 20,
    "subjects":["maths","chem","java"]
#  key: value          items
}
print(biodata["name"])
print(biodata["subjects"])
print(biodata["age"])

for i in biodata:
    print(biodata[i])

print(biodata[1]) # error