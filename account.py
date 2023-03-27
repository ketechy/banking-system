class Account:
    def __init__(self, number, balance=0.0):
        """
        Initializes a new Account object with the given number and balance.

        Args:
        number (int): The account number.
        balance (float): The initial account balance (default 0.0).
        """
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits the given amount into the account and returns the new balance.

        Args:
        amount (float): The amount to be deposited.

        Returns:
        The new balance after the deposit.
        """
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """
        Withdraws the given amount from the account if the balance is sufficient.

        Args:
        amount (float): The amount to be withdrawn.

        Returns:
        If the balance is sufficient, returns the new balance after the withdrawal.
        Otherwise, returns the string 'Insufficient balance'.
        """
        if self.balance < amount:
            return 'Insufficient balance'
        else:
            self.balance -= amount
            return self.balance
