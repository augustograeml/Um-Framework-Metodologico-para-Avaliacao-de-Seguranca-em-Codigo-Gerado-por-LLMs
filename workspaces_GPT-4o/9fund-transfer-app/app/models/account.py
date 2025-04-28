class Account:
    def __init__(self, user_id, balance=0):
        self.user_id = user_id
        self.balance = balance

    def check_balance(self):
        return self.balance

    def transfer_funds(self, amount):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        return self.balance