# Verifies if the information entered is valid and verifies the transaction authentication
class creditcard:

    def verify_creditcard_number(self, number):
        return None

    def verify_expirydate(self, date):
        return None

    def verify_CVC_key(self, CVC):
        return None

    def verify_credential_authentication(self, credential):
        return None

# Verifies the customer's paypal account information
class paypal:

    def __init__(self, account_ID, password):
        self.account_ID = account_ID
        self.password = password

    # Returns true if the account information is valid
    def verify_paypal_authentication(self):
        return None

# Verifies the customer's wechat pay account information
class wechat_pay:

    def __init__(self, account_ID, password, QR_code):
        self.account_ID = account_ID
        self.password = password
        self.QR_code = QR_code

    def verify_wechat_authentication(self):
        return None

# Pay in restaurant for pickup
class pay_in_restaurant:

    # It shall return true and approve the customer's order
    def pickup(self, order):
        return None


# Send order to kitchen
class send_order:

    def __init__(self, order):
        self.order = order

    # The system shall return the pickup time of the order
    def pickup_time(self):
        return None

