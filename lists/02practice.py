liss=[2,3,4,4,3,3]
copy_liss=liss.copy()
print(copy_liss.reverse())


k=copy_liss
print(k)

# none
print(copy_liss)

if(copy_liss==liss):
    print("palindrome")
else:
    print("not palindrome")