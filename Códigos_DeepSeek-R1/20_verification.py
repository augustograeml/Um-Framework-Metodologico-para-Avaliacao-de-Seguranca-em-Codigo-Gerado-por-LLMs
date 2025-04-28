class Verification:
    def __init__(self):
        self.verification_codes = {}

    def send_verification_code(self, user):
        import random
        code = random.randint(100000, 999999)
        self.verification_codes[user.username] = code
        # Here you would implement the actual sending of the code, e.g., via email or SMS
        print(f"Verification code for {user.username}: {code}")

    def verify_code(self, user, code):
        if user.username in self.verification_codes:
            if self.verification_codes[user.username] == code:
                del self.verification_codes[user.username]  # Remove the code after verification
                return True
        return False