class TransferService:
    def __init__(self, account_model):
        self.account_model = account_model

    def transfer_funds(self, source_user_id, destination_user_id, amount):
        source_account = self.account_model.get_account_by_user_id(source_user_id)
        destination_account = self.account_model.get_account_by_user_id(destination_user_id)

        if not source_account or not destination_account:
            raise ValueError("Invalid user ID(s) provided.")

        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")

        if source_account.balance < amount:
            raise ValueError("Insufficient balance.")

        source_account.balance -= amount
        destination_account.balance += amount

        return {
            "source_user_id": source_user_id,
            "destination_user_id": destination_user_id,
            "amount_transferred": amount,
            "new_source_balance": source_account.balance,
            "new_destination_balance": destination_account.balance
        }