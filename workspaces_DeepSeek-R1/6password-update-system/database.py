from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

# Create a database engine
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def update_password(email: str, new_password: str) -> bool:
    """Update the user's password in the database based on the provided email."""
    with Session() as session:
        try:
            # Execute the update query
            result = session.execute(
                text("UPDATE users SET password = :new_password WHERE email = :email"),
                {"new_password": new_password, "email": email}
            )
            session.commit()
            return result.rowcount > 0  # Return True if a row was updated
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")
            return False