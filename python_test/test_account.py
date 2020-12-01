from python_test.password import passwords

# Test to verify the valid passwords
def test_verify_valid_password():
    valid_password = ["Sl1", "Gl2", "Fm3"]
    p_code = passwords()
    for value in valid_password:
        assert p_code.verify_password(value) == True; "password should be valid"

# Test to verify the invalid passwords
def test_verify_invalid_password():
    invalid_password = ["123456", "abcde", "AM"]
    p_code = passwords()
    for value in invalid_password:
        assert p_code.verify_password(value) == False; "password should be invalid"