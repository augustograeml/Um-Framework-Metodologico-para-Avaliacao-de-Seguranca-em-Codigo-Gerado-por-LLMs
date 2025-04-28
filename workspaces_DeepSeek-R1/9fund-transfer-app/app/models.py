class User:
    def __init__(self, user_id, balance):
        self.user_id = user_id
        self.balance = balance

    def transfer_funds(self, destination_user, amount):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        destination_user.balance += amount

    def __repr__(self):
        return f"User({self.user_id}, Balance: {self.balance})"