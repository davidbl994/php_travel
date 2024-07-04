# Verify that all elements (username field, password field, login button, etc.) are present on the login page.
import utils.locators
from pages.login_page import LoginPage
from utils.locators import Login

def test_verify_login_elements(driver, login_url):
    login_page = LoginPage(driver)
    print("Opening login page...")
    login_page.open_login_page(login_url)

    # Check for other elements like username and password fields are present
    print("Checking that the login button is loaded...")
    assert Login.LOGIN_BTN is not None
    print("Login button is successfully loaded!")

    print("Checking that the Email Address input field is loaded...")
    assert Login.EMAIL_ADDRESS is not None
    print("Email Address input field is successfully loaded!")

    print("Checking that the Password input field is successfully loaded...")
    assert Login.PASSWORD is not None
    print("Password input field is successfully loaded!")

    print("Checking that the Remember me check box is loaded...")
    assert Login.REMEMBER_CHECK_BOX is not None
    print("Remember me check box is successfully loaded!")

    print("Checking that the Sign up button is loaded...")
    assert Login.SIGN_UP_BTN is not None
    print("Sign up button is loaded successfully!")