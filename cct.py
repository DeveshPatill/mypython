class Customer:
    def __init__(self, customer_id, customer_name):
        self.customer_id = customer_id
        self.customer_name = customer_name

    def display_customer_info(self):
        return f"Customer ID: {self.customer_id} Customer Name: {self.customer_name}"


class CreditCard(Customer):
    def __init__(self, customer_id, customer_name, card_type, card_number):
        super().__init__(customer_id, customer_name)
        self.card_type = card_type
        self.card_number = card_number

    def display_card_info(self):
        return f"Card Type: {self.card_type} Card Number: {self.card_number}"


class Transaction(CreditCard):
    def __init__(self, customer_id, customer_name, card_type, card_number, transaction_id, amount):
        super().__init__(customer_id, customer_name, card_type, card_number)
        self.transaction_id = transaction_id
        self.amount = amount

    def display_transaction_info(self):
        return f"Transaction ID: {self.transaction_id} Amount: {self.amount}"

    def update_amount(self, new_amount):
        self.amount = new_amount
        return f"Transaction {self.transaction_id} updated to amount {self.amount}"


class TransactionSummary(Transaction):
    def __init__(self, customer_id, customer_name):
        self.transactions = []
        self.customer_id = customer_id
        self.customer_name = customer_name

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def calculate_total_amount(self):
        return sum(t.amount for t in self.transactions)

    def display_summary(self):
        # Display customer info
        print(f"Customer ID: {self.customer_id} Customer Name: {self.customer_name}")
        # Display details grouped by card
        for t in self.transactions:
            print(t.display_card_info())
            print(t.display_transaction_info())
        # Display total
        print(f"Total Transaction Amount: {self.calculate_total_amount()}")


# ------------------- DEMO -------------------

# Create transaction summary for one customer
summary = TransactionSummary("C301", "Michael Brown")

# Add transactions
t1 = Transaction("C301", "Michael Brown", "Visa", "123456789012", "T001", 1500)
t2 = Transaction("C301", "Michael Brown", "Visa", "123456789012", "T002", 2200)
t3 = Transaction("C301", "Michael Brown", "Amex", "987654321098", "T003", 1800)

summary.add_transaction(t1)
summary.add_transaction(t2)
summary.add_transaction(t3)

# Update one transaction (bonus feature)
print(t2.update_amount(2500))  # Increase T002 from 2200 to 2500

# Display everything
summary.display_summary()
