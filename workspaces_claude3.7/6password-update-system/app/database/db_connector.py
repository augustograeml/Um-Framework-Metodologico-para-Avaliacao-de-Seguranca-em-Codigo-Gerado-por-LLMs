from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import os

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def get_db_session():
    session = Session()
    try:
        yield session
    except SQLAlchemyError as e:
        session.rollback()
        raise e
    finally:
        session.close()