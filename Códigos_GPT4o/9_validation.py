def is_positive_amount(amount):
    return isinstance(amount, (int, float)) and amount > 0

def is_valid_user_id(user_id, existing_user_ids):
    return user_id in existing_user_ids

def validate_transfer_input(user_id, amount, existing_user_ids):
    if not is_valid_user_id(user_id, existing_user_ids):
        raise ValueError("Invalid user ID.")
    if not is_positive_amount(amount):
        raise ValueError("Amount must be a positive number.")
    return True