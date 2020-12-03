# This test file tests the requirements of the account features

from python_test.account import passwords
from python_test.account import accounts
from python_test.account import order

# Test to verify the valid passwords which consists of at least 8 characters
# It must include an upper case letter, lower case letter and a number
# Requirement 5.1.3
def test_verify_valid_password():
    valid_password = ["Sabc13579", "Bmwac34567", "Aclaw1122"]
    p_word = passwords()
    for passcode in valid_password:
        assert p_word.verify_password(passcode) == True, "password should be valid"


# Test to verify the invalid passwords
def test_verify_invalid_password():
    invalid_password = ["123456", "abcdef", "McMaster", None]
    p_word = passwords()
    for passcode in invalid_password:
        assert p_word.verify_password(passcode) == False, "password should be invalid"


# Test to verify the valid accounts with unique account information
# Account object includes account(username, password, confirm password, email, phone number)
# Requirement 3.1.1
def test_valid_unique_account():
    account_1 = accounts("McMaster123", "Scba123456", "Scba123456", "suofqpd1200@gmail.com", "John Doe", "416-956-8837")
    account_2 = accounts("McMaster456", "Scba123456", "Scba123456", "wings1122@gmail.com", "Rick Lee", "416-985-8531")
    account_1.create_account()  # Creates the first account
    assert account_2.verify_account() == True, "account information should be valid"


# Test to verify an invalid account
# It will be done by testing 2 accounts with the same username
# Requirement 3.1.1
def test_invalid_account_1():
    account_1 = accounts("McMaster123", "Scba123456", "Scba123456", "suofqpd1200@gmail.com", "John Doe", "416-956-8837")
    account_2 = accounts("McMaster123", "Sabc123456", "Sabc123456", "suofqpd1500@gmail.com", "Rob Doe", "416-988-8815")
    account_1.create_account()  # Creates the first account
    assert account_2.verify_account() == False, "account information should be invalid as it's not unique"


# Test to verify another invalid account
# It will be done by testing 1 account with different passwords for confirmation
# Requirement 3.1.1
def test_invalid_account_2():
    account_1 = accounts("McMaster123", "Scba123456", "ABCas123456", "suofqpd1200@gmail.com", "John Doe", "416-956-8837")
    assert account_1.verify_account() == False, "account information should be invalid as the passwords are different"


# Test to verify if the system changes the old password to the new password for requirement 3.1.3
def test_change_password():
    account_1 = accounts("McMaster123", "Scba123456", "Scba123456", "suofqpd1200@gmail.com", "John Doe", "416-956-8837")
    old = "Scba123456"
    new = "ABc1234567"
    assert account_1.password_change(old, new) == new, "password should be changed to the new password"


# Test if the profile is changed by changing the email address
# Requirement 3.1.3
def test_change_profile():
    account_1 = accounts("McMaster456", "Scba123456", "Scba123456", "wings1122@gmail.com", "Rick Lee", "416-985-8531")
    account_1.change_profile("Mcmaster456", "sdcasfef117@mcmaster.ca", "Rick Lee", "416-985-8531")
    assert account_1.email == "sdcasfef117@mcmaster.ca", "email should be changed to the new email"


# Test if the login system can correctly interpret the username/email and password the user entered
# Requirement 3.1.2
# Test a valid login information
def test_login_authentication_valid():
    account_1 = accounts("McMaster456", "Scba123456", "Scba123456", "wings1122@gmail.com", "Rick Lee", "416-985-8531")
    assert account_1.login("McMaster456", "Scba123456") == True, "login information should be correct"

# Test an invalid login information where the password the user entered is incorrect
def test_login_authentication_invalid():
    account_1 = accounts("McMaster456", "Scba123456", "Scba123456", "wings1122@gmail.com", "Rick Lee", "416-985-8531")
    assert account_1.login("McMaster456", "Scale1122") == False, "login information should be incorrect"


# Test if the system returns the correct order information for an order ID in order history
# Order class includes order(username, order ID, order time, order items, total price)
# Requirement 3.1.4
def test_view_order_history():
    # Account
    account_1 = accounts("McMaster123", "Scba123456", "Scba123456", "suofqpd1200@gmail.com", "John Doe", "416-956-8837")
    # Creates an order for the account
    items = ["Hamburger", "Smoothie", "Pizza", "Salad", "Ice Cream"]
    order_1 = order("McMaster123", 369, "September 3, 2020 at 6:30PM", items, 55.99)
    assert account_1.view_order_history(369) == order_1, "it shall display the information of order_1 for account_1"



