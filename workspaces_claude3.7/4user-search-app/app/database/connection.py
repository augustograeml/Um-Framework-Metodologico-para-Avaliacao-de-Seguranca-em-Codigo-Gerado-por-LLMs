from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///users.db"  # Update with your database URL

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def get_session():
    return Session()

def close_session(session):
    session.close()