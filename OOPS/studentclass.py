class student:
    college_name = "SSS"
    # college name is a class attribute... as it applicable for all the objects of the class
    name="anonymous" #class attribute

    def __init__(self, name, marks):
        self.name=name  #object attribute has more presidence than class attribute
        self.marks=marks
        print("adding new sytudent in database...")
    # 
s1=student("manoj",50)
print(s1.name,s1.marks,s1.college_name)
print(s1)

s2=student("karan",62)
print(s2.name,s2.marks,s2.college_name)

# s3=student(  44)
# print(s3.name,s3.marks)

print(student.college_name)
student.no_of_students=50                       #class attribute can also be created outside the class and can be accessed afterwards
print(student.no_of_students)