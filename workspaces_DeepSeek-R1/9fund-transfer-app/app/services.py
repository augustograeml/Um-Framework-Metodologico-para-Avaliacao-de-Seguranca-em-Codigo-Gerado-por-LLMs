def transfer_funds(current_user, destination_user_id, amount):
    if amount <= 0:
        return "Transfer amount must be greater than zero."
    
    if current_user.balance < amount:
        return "Insufficient balance."
    
    destination_user = User.query.filter_by(id=destination_user_id).first()
    
    if not destination_user:
        return "Destination user not found."
    
    current_user.balance -= amount
    destination_user.balance += amount
    
    db.session.commit()
    
    return "Transfer successful."