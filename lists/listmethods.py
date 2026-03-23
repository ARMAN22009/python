# append
list=[22,33,25,9,2,33]
list.append(100)
print(list)

a=list
a.append(500)
print(a)
# sort
list.sort()
print(list)

print(list.sort(reverse=True))
print(list)

print(list.reverse())
print(list)

list.insert(2,55)
print(list)

list.remove(33)
print(list)

list.pop(4)                 # remooves at iundex 4
print(list)