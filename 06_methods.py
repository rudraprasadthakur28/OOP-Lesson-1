def greet():  # This is a function
    print("Hello")

greet()

class S:  # class

    def study(self):  # This is also a function but this is inside class so it is a method
        print("Student is studying")

s1 = S()  # student1 = object
s1.study()  # calling the method

class Student():
    def __init__(self, name):
        self.name = name

    def study(self):
        print(self.name, "is studying")

student1 = Student("Rudra")
student2 = Student("Rahul")

student1.study()
student2.study()