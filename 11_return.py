# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#     def get_balance(self):
#         return self.balance
# account1 = BankAccount("Rudra",50000)
# result = account1.get_balance()
# print(result)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_age(self):
        return self.age
student1 = Student("Rudra", 27)
result = student1.get_age()
print(result)

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def get_balance(self):
        return self.balance
account1 = BankAccount("Rudra",50000)
result = account1.get_balance()
print(result)