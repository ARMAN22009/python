text = "  hello world  "
print(text.strip())  
# Output: 'hello world'

text2 = "xyxhelloxy"
print(text2.strip("xy"))  
# Output: 'hello'


text3="chchchcyhhhhhcccc"

print(text3.strip("c"))

k=text3.strip("c")
print(k.strip("h"))