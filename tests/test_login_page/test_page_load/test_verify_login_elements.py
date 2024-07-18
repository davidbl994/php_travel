from utils.locators import Login
from pages.login_page import logger

def test_verify_login_elements(driver, login_page):

    logger.info("Checking that the login button is loaded...")
    assert Login.LOGIN_BTN is not None, "Login button element is not found or defined"
    logger.info("Login button is successfully loaded!")

    logger.info("Checking that the Email Address input field is loaded...")
    assert Login.EMAIL_ADDRESS is not None, "Email Address input field element is not found or defined"
    logger.info("Email Address input field is successfully loaded!")

    logger.info("Checking that the Password input field is loaded...")
    assert Login.PASSWORD is not None, "Password input field element is not found or defined"
    logger.info("Password input field is successfully loaded!")

    logger.info("Checking that the Remember me check box is loaded...")
    assert Login.REMEMBER_CHECK_BOX is not None, "Remember me check box element is not found or defined"
    logger.info("Remember me check box is successfully loaded!")

    logger.info("Checking that the Sign up button is loaded...")
    assert Login.SIGN_UP_BTN is not None, "Sign up button element is not found or defined"
    logger.info("Sign up button is loaded successfully!")