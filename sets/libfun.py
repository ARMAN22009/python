call=set()

set2={33,44,990}
call.add(44)
call.add(5)
call.add(4090900000000)
call.add("manuganu")
# call.add([333,444])
# unhasable type |LIST| so cnnot be added

# call.add({331113,444})
# unhasable type |SETS| so cnnot be added
print(call)

call.remove(5)
print(call)


print(call.union(set2))

print(call.intersection(set2))

print(call.pop())
#Removes and returns a random element (since sets are unordered).

call.clear()
print(call.clear())

