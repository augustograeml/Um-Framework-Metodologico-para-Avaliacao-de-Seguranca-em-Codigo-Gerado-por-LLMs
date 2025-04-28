# main.py

from auth.login import Login
from auth.verification import Verification

def main():
    login = Login()
    verification = Verification()

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if login.authenticate_user(username, password):
        user_id = username  # Assuming user_id is the same as username for simplicity
        verification_code = verification.generate_verification_code(user_id)
        
        print(f"Verification code sent to your registered email: {verification_code}")
        entered_code = input("Enter the verification code: ")

        if verification.validate_verification_code(user_id, entered_code):
            print("Login successful!")
        else:
            print("Invalid verification code.")
    else:
        print("Authentication failed. Please check your username and password.")

if __name__ == "__main__":
    main()