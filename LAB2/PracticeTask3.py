class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")

    def get_balance(self):
        return self.__balance


account1 = BankAccount(1000)
account2 = BankAccount(500)
account3 = BankAccount(2000)


print("Account 1:")
account1.deposit(500)
account1.withdraw(200)
print(f"Balance: {account1.get_balance()}")

print()


print("Account 2:")
account2.deposit(300)
account2.withdraw(100)
print(f"Balance: {account2.get_balance()}")

print()


print("Account 3:")
account3.deposit(1000)
account3.withdraw(500)
print(f"Balance: {account3.get_balance()}")

