class TransferService:
    def __init__(self, user_repository, account_repository):
        self.user_repository = user_repository
        self.account_repository = account_repository

    def validate_transfer(self, user_id, destination_user_id, amount):
        user = self.user_repository.get_user_by_id(user_id)
        destination_user = self.user_repository.get_user_by_id(destination_user_id)

        if not user or not destination_user:
            raise ValueError("Invalid user ID(s) provided.")

        if amount <= 0:
            raise ValueError("Transfer amount must be greater than zero.")

        if user.balance < amount:
            raise ValueError("Insufficient balance for the transfer.")

        return True

    def execute_transfer(self, user_id, destination_user_id, amount):
        self.validate_transfer(user_id, destination_user_id, amount)

        user_account = self.account_repository.get_account_by_user_id(user_id)
        destination_account = self.account_repository.get_account_by_user_id(destination_user_id)

        user_account.balance -= amount
        destination_account.balance += amount

        self.account_repository.update_account(user_account)
        self.account_repository.update_account(destination_account)

        return {
            "message": "Transfer successful",
            "from": user_id,
            "to": destination_user_id,
            "amount": amount
        }