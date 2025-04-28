def search_users_by_name(db_session, name):
    return db_session.query(User).filter(User.name.ilike(f"%{name}%")).all()

def search_users_by_email(db_session, email):
    return db_session.query(User).filter(User.email.ilike(f"%{email}%")).all()

def search_users(db_session, name=None, email=None):
    query = db_session.query(User)
    
    if name:
        query = query.filter(User.name.ilike(f"%{name}%"))
    
    if email:
        query = query.filter(User.email.ilike(f"%{email}%"))
    
    return query.all()