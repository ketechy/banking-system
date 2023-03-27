from bank import Bank
from customer import Customer
from account import Account
from savings_account import SavingsAccount

# Create a new bank object
bank = Bank('My Bank')

# Create a new customer object
customer = Customer(1, 'John')

# Add the customer to the bank
bank.add_customer(customer)

# Create a new savings account object
savings_account = SavingsAccount(1001)

# Add the savings account to the customer
customer.add_account(savings_account)

# Deposit some money into the savings account
savings_account.deposit(1000)

# Add interest to the savings account
savings_account.add_interest()

# Get the savings account balance
balance = savings_account.balance

# Print the savings account balance
print(f'The savings account balance is {balance}')