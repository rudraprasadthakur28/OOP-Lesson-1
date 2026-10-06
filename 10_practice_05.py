class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def show_balance(self):
        print(f"{self.name}'s balance is {self.balance}")
account1 = BankAccount("Rudra", 50000)
account1.show_balance()