def main():
    import sqlite3
    from app.database import create_connection, create_user_table
    from app.utils import hash_password, verify_password

    # Connect to the SQLite database
    conn = create_connection("users.db")
    
    # Create user table if it doesn't exist
    create_user_table(conn)

    while True:
        print("Welcome to the Login System")
        choice = input("Do you want to (1) Login or (2) Register? (q to quit): ")

        if choice == '1':
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            cursor = conn.cursor()
            cursor.execute("SELECT password FROM users WHERE username=?", (username,))
            result = cursor.fetchone()

            if result and verify_password(password, result[0]):
                print("Login successful!")
            else:
                print("Invalid username or password.")

        elif choice == '2':
            username = input("Choose a username: ")
            password = input("Choose a password: ")
            hashed_password = hash_password(password)

            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
            print("Registration successful!")

        elif choice.lower() == 'q':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()