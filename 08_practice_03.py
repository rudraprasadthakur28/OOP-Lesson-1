class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"{self.name} is {self.age} years old")

student1 = Student("Rudra",27)
student1.introduce()