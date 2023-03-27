class Customer:
    def __init__(self, id, name):
        """
        Initializes a new Customer object with the given ID and name.

        Args:
        id (int): The ID of the customer.
        name (str): The name of the customer.
        """
        self.id = id
        self.name = name
        # Initialize an empty list of accounts
        self.accounts = []

    def add_account(self, account):
        """
        Adds the given Account object to the list of accounts.

        Args:
        account (Account): The Account object to be added.
        """
        self.accounts.append(account)
