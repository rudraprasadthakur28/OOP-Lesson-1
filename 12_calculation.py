# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def get_new_balance(self, amount):
#         return self.balance + amount

# account1 = BankAccount("Rudra", 50000)

# result = account1.get_new_balance(5000)

# print(result)

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_total(self, amount):
        return self.balance + amount

account1 = BankAccount("Rudra", 50000)

result = account1.get_total(10000)

print(result)