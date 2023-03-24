class Account:
    def __init__(self, number, balance=0.0):
        self.number = number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if self.balance < amount:
            return 'Insufficient balance'
        else:
            self.balance -= amount
            return self.balance