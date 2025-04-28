class SearchService:
    def __init__(self, db_session):
        self.db_session = db_session

    def search_by_name(self, name):
        return self.db_session.query(User).filter(User.name.ilike(f'%{name}%')).all()

    def search_by_email(self, email):
        return self.db_session.query(User).filter(User.email.ilike(f'%{email}%')).all()

    def search(self, query):
        results = []
        if query:
            results.extend(self.search_by_name(query))
            results.extend(self.search_by_email(query))
        return results