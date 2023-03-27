from account import Account

class SavingsAccount(Account):
    def __init__(self, number, balance=0.0, interest_rate=0.01):
        """
        Initializes a new SavingsAccount object with the given number, balance, and interest rate.

        Args:
        number (int): The account number.
        balance (float): The initial account balance (default 0.0).
        interest_rate (float): The interest rate for the account (default 0.01).
        """
        super().__init__(number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        """
        Adds interest to the account based on the current balance and interest rate.

        Returns:
        The amount of interest added to the account balance.
        """
        interest = self.balance * self.interest_rate
        self.balance += interest
        return interest
