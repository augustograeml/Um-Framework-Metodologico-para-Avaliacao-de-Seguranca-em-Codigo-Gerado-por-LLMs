class User:
    def __init__(self, user_id, username, balance):
        self.id = user_id
        self.username = username
        self.balance = balance

    def transfer_funds(self, amount, destination_user):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance for transfer.")
        
        self.balance -= amount
        destination_user.balance += amount
        return True

    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}', balance={self.balance})"