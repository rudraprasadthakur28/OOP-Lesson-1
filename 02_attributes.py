class Student:  # Blueprint
    pass

student1 = Student()  # student1 = object
student2 = Student()
# Attribute = Object ke andar stored data/information.
student1.name = "Rudra"  # name = attribute
student1.age = 27  # age = attribute

student2.name = "Rahul"
student2.age = 22

print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)

# Class = Blueprint / Template

# Object = Class se bani actual instance

# Attribute = Object ke andar stored data/information

class Student:
    pass

student1 = Student()

student1.name = "Rudra"  # student1 = object
student1.age = 27  # age = attribute
student1.course = "CSE"  # CSE = value
student1.city = "Mallarpur"

print(student1.name)
print(student1.age)
print(student1.course)
print(student1.city)