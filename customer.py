class Customer:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)