class Student:
    def __init__(self, name, age, course):  # self current object ko refer karta hain
        self.name = name
        self.age = age
        self.course = course  
        # name, age, course object banate waqt milne wali values ko receive kar rahe hain

student1 = Student("Rudra", 27, "CSE")

print(student1.name)
print(student1.age)
print(student1.course)

