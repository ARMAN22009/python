values={9,"9.0"}
print(values)
# both 9,9.0 are interpreted different as one of them is a string and another is a integer

marks={33,33.00}
print(marks)
print(type(marks[0]))
# both 33,33.00 are interpreted same 

# can also  be stored as tuples
balls={
    "float":90.00,
    "integer":90,

}
print(balls)