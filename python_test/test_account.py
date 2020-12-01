from python_test.account import passwords

# Test to verify the valid passwords
def test_verify_valid_password():
    p_code = passwords("Sabc13579")
    assert p_code.verify_password() == True, "password should be valid"


# Test to verify the invalid passwords
def test_verify_invalid_password():
    p_code = passwords("123456")
    assert p_code.verify_password() == False, "password should be invalid"


def test_change_password():
    p_code = passwords("S123456mac")
    new_password = "ABc1234567"
    assert p_code.password_change(new_password) == "ABc1234567", "password should be changed to the new password"
