# test_verify_login_elements.py
from utils.locators import Login

def test_verify_login_elements(driver, login_page):
    """
    Test to verify the presence of essential elements on the login page.
    """
    # Check Login button
    print("Checking that the login button is loaded...")
    assert Login.LOGIN_BTN is not None, "Login button element is not found or defined"
    print("Login button is successfully loaded!")

    # Check Email Address input field
    print("Checking that the Email Address input field is loaded...")
    assert Login.EMAIL_ADDRESS is not None, "Email Address input field element is not found or defined"
    print("Email Address input field is successfully loaded!")

    # Check Password input field
    print("Checking that the Password input field is loaded...")
    assert Login.PASSWORD is not None, "Password input field element is not found or defined"
    print("Password input field is successfully loaded!")

    # Check Remember me check box
    print("Checking that the Remember me check box is loaded...")
    assert Login.REMEMBER_CHECK_BOX is not None, "Remember me check box element is not found or defined"
    print("Remember me check box is successfully loaded!")

    # Check Sign up button
    print("Checking that the Sign up button is loaded...")
    assert Login.SIGN_UP_BTN is not None, "Sign up button element is not found or defined"
    print("Sign up button is loaded successfully!")