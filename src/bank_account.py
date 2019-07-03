class BankAccount:
    def __init__(self, account_type, amount):
        self.account_type = account_type
        self.amount = amount

    def deposit(self, deposit_amount):
        self.amount += deposit_amount
    
    def withdraw(self, withdraw_amount):
        self.amount -= withdraw_amount
    
    def __str__(self):
        return "{} Amount: {}".format(self.account_type, self.amount)

account = BankAccount("checkings", 100)
print(account.account_type)
print(account.amount)

account.deposit(30)
print(account.amount)

account.withdraw(50)
print(account.amount)

print(account)
