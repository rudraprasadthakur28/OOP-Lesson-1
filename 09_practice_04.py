class Student:
    def __init__(self, name):
        self.name = name
    def study(self, subject):
        print(f"{self.name} is studying {subject}")

student1 = Student("Rudra")
student1.study("Python")