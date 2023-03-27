import unittest
from bank import Bank
from customer import Customer
from account import Account
from savings_account import SavingsAccount

class TestBankingSystem(unittest.TestCase):
    def test_account_deposit(self):
        account = Account(1, 100)
        balance = account.deposit(50)
        self.assertEqual(balance, 150)

    def test_savings_account_add_interest(self):
        savings_account = SavingsAccount(1001, 1000, 0.01)
        interest = savings_account.add_interest()
        self.assertEqual(interest, 10.0)
        self.assertEqual(savings_account.balance, 1010.0)

    def test_bank_add_customer_and_get_customer(self):
        bank = Bank('My Bank')
        customer = Customer(1, 'John')
        bank.add_customer(customer)
        retrieved_customer = bank.get_customer(1)
        self.assertEqual(retrieved_customer, customer)

if __name__ == '__main__':
    unittest.main()
