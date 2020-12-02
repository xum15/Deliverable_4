class passwords:

    # takes a password and returns True if valid, False otherwise
    def verify_password(self, password):
        return None

    # changes the password
    def password_change(self, old_password, new_password):
        return None

class accounts(passwords):
    
    def __init__(self, username, password, confirm_password, email, name, phone):
        self.username = username
        self.password = password
        self.confirm_password = confirm_password
        self.email = email
        self.name = name
        self.phone = phone

    # Returns True if the information satisfies requirement 3.1.1
    # Returns False otherwise
    def verify_account(self):
        return None

    # Creates account
    def create_account(self):
        return None

    # Changes profile in which the user can change any information listed below
    def change_profile(self, username, email, name, phone):
        return None

    # Login system where the user enters their username/email and password
    # Returns true if the login information is correct and false otherwise
    def login(self, username_or_email, password):
        return None