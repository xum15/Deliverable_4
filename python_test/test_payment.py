from python_test.payment import creditcard
from python_test.payment import paypal
from python_test.payment import wechat_pay
from python_test.payment import pay_in_restaurant
from python_test.payment import send_order
from python_test.account import order

# Test valid credit card numbers
# Requirement 3.2.2.1
def test_valid_creditcard_number():
    valid_number = [4520038156423956, 4105865219623654, 4562321056428926]
    card_number = creditcard()
    for number in valid_number:
        assert card_number.verify_creditcard_number(number) == True, "Credit card number should be valid"

# Test invalid credit card numbers
def test_invalid_creditcard_number():
    invalid_number = [85632, 123456, "8888", 9832.667, None]
    card_number = creditcard()
    for number in invalid_number:
        assert card_number.verify_creditcard_number(number) == False, "Credit card number should be invalid"

# Test valid credit card expiry dates
def test_valid_expirydate():
    valid_expdate = ["2/23", "6/25", "8/3", "5/29", "12/30"]
    card_date = creditcard()
    for date in valid_expdate:
        assert card_date.verify_expirydate(date) == True, "Credit card expiry date should be valid"

# Test invalid credit card expiry dates
def test_invalid_expirydate():
    invalid_expdate = ["18/23", "6/35", "855", "Date", None]
    card_date = creditcard()
    for date in invalid_expdate:
        assert card_date.verify_expirydate(date) == False, "Credit card expiry date should be invalid"

# Test valid credit card CVC keys
def test_valid_CVC_key():
    valid_CVC = [138, 939, 199, 885, 500]
    CVC_key = creditcard()
    for CVC in valid_CVC:
        assert CVC_key.verify_CVC_key(CVC) == True, "Credit card CVC key should be valid"

# Test invalid credit card CVC keys
def test_invalid_CVC_key():
    invalid_CVC = [13, 9, "word", "McMaster", None]
    CVC_key = creditcard()
    for CVC in invalid_CVC:
        assert CVC_key.verify_CVC_key(CVC) == False, "Credit card CVC key should be invalid"


# Test if the system can verify the correct credential information
# Credential information is shown in the following order:
# Name, credit card number, expiry date, CVC key
def test_verify_valid_credential_authentication():
    correct_credential = [
        "John Doe",
        4520038156423956,
        "2/23",
        199
    ]

    card = creditcard()
    assert card.verify_credential_authentication(correct_credential) == True, "Credit card information is correct"


# Test if the system can verify the incorrect credential information
# The credit card information is valid but the account does not exist
def test_verify_invalid_credential_authentication():
    incorrect_credential = [
        "John Doe",
        4520038156423988,
        "2/26",
        298
    ]

    card = creditcard()
    assert card.verify_credential_authentication(incorrect_credential) == False, "Credit card information is incorrect"


# Test if the system can verify a valid paypal account
def test_verify_valid_paypal_account():
    valid_account = paypal("aquaman1122@gmail.com", "McMaster321$")
    assert valid_account.verify_paypal_authentication() == True, "The paypal account information should be valid"


# Test if the system can verify an invalid paypal account with the incorrect password
def test_verify_invalid_paypal_account():
    invalid_account = paypal("aquaman1122@gmail.com", "McMaster3388")
    assert invalid_account.verify_paypal_authentication() == False, "The paypal account information should be invalid"

# Test if the system can verify a valid wechat account
def test_verify_valid_wechat_account():
    valid_account = wechat_pay("aquaman8888", "McMaster321$", "QR Code")
    assert valid_account.verify_wechat_authentication() == True, "The wechat account information should be valid"


# Test if the system can verify an invalid wechat account with the incorrect username
def test_verify_invalid_wechat_account():
    invalid_account = wechat_pay("aquaman1122", "McMaster321$", "QR Code")
    assert invalid_account.verify_wechat_authentication() == False, "The wechat account information should be invalid"


# Test if the system can approve the customer's order if they chose to pay in restaurant for pickup
# Requirement 3.2.4
def test_pay_in_restaurant_for_pickup():
    items = ["Hamburger", "Smoothie", "Pizza", "Salad", "Ice Cream"]
    order_1 = order("McMaster123", 369, "September 3, 2020 at 6:30PM", items, 55.99)
    payment = pay_in_restaurant()
    assert payment.pickup(order_1) == True, "The customer's order and payment method should be approved"


# Test if the system can display the estimated pickup time for the customer's order that was sent to the kitchen
# Requirement 3.2.5.1
def test_pickup_time_estimation():
    items = ["Hamburger", "Smoothie", "Pizza", "Salad", "Ice Cream"]
    order_1 = order("McMaster123", 369, "September 3, 2020 at 6:30PM", items, 55.99)
    send_order_1 = send_order(order_1)
    pickup_time = "6:30PM"
    assert send_order_1.pickup_time() == pickup_time, "The estimated pickup time should be displayed"
