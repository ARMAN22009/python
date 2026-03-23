resume ={
    "name":"Arman",
    "age":"20",
    "sex":"male",
}

print(resume.items())


print(resume.get("age"))
# none
print(resume["age"])
# error 

resume.update({"adress":"KOLKATA","name":"Manoj"})
print(resume)