class Person:
    def __init__(self, name, age):
        self.__name = name     # private attribute
        self.__age = age       # private attribute

    # Getter method (to read private data)
    def get_age(self):
        return self.__age

    # Setter method (to update private data)
    def set_age(self, new_age):
        if new_age > 0:                                 # provides us with the  if condition 
            self.__age = new_age
        else:
            print("Age must be positive")

p1 = Person("Arman", 21)

# print(p1.__age)         ❌ Error: can't access private attribute
print(p1.get_age())       # ✅ Access via getter 

p1.set_age(25)            # ✅ Update via setter
print(p1.get_age())       # 25
