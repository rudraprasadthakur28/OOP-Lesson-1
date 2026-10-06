# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         return self.balance + amount

# account1 = BankAccount("Rudra",50000)

# new_balance = account1.deposit(10000)

# print(f"{account1.name}'s total balance is {new_balance}")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def get_salary(self):
        return self.salary
employee1 = Employee("Rudra",30000)
result = employee1.get_salary()
print(f"{employee1.name}'s salary is {result}")

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount

account1 = BankAccount("Rudra", 50000)

account1.deposit(10000)

print(account1.balance)

class Calculator:
    def multiply(self, a, b):
        return a * b
calculator1 = Calculator()

result = calculator1.multiply(10, 5)

print(result)