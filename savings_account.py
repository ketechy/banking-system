from account import Account

class SavingsAccount(Account):
    def __init__(self, number, balance=0, interest_rate=0.01):
        super().__init__(number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return interest