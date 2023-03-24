class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []
    
    def add_customer(self, customer):
        self.customers.append(customer)

    def get_customer(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                return customer
        return None