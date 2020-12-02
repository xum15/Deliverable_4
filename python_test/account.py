class passwords:

    # takes a password and returns True if valid, False otherwise
    def verify_password(self, password):
        return None

    # changes the password
    def password_change(self, old_password, new_password):
        return None

class order():

    def __init__(self, username, order_ID, order_time, order_items, total_cost):
        self.username = username
        self.order_ID = order_ID
        self.order_time = order_time
        self.order_items = order_items
        self.total_cost = total_cost

    # Customer should be able to view any or the orders they made
    # It shall display the order information of the selected order ID
    def view_order_history(self, order_ID):
            return None


class accounts(passwords, order):
    
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
