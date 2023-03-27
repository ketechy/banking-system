class Bank:
    def __init__(self, name):
        """
        Initializes a new Bank object with the given name.

        Args:
        name (str): The name of the bank.
        """
        self.name = name
        # Initialize an empty list of customers
        self.customers = []

    def add_customer(self, customer):
        """
        Adds the given Customer object to the list of customers.

        Args:
        customer (Customer): The Customer object to be added.
        """
        self.customers.append(customer)

    def get_customer(self, customer_id):
        """
        Finds the Customer object with the given ID in the list of customers.

        Args:
        customer_id (int): The ID of the customer to be retrieved.

        Returns:
        The Customer object with the given ID if found, None otherwise.
        """
        for customer in self.customers:
            if customer.id == customer_id:
                return customer
        # If no Customer object with the given ID is found, return None
        return None
