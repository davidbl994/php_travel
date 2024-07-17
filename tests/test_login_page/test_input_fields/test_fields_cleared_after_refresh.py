import pytest
from pages.login_page import logger
from utils.config import USERNAME, PASSWORD
from utils.locators import Login

@pytest.mark.usefixtures("driver")
def test_input_fields_cleared_on_refresh(driver, login_page):

    logger.info("Inserting email...")
    login_page.insert_email(USERNAME)
    logger.info("Email inserted!")

    logger.info("Inserting password...")
    login_page.insert_password(PASSWORD)
    logger.info("Password inserted")

    logger.info("Refreshing web page...")
    driver.refresh()
    logger.info("Web page refreshed!")

    email_field = driver.find_element(*Login.EMAIL_ADDRESS)
    password_field = driver.find_element(*Login.PASSWORD)

    logger.info("Checking email field is cleared...")
    assert email_field.get_attribute('value') == "", "Email field is not cleared"
    logger.info("Email field is cleared!")

    logger.info("Checking password field is cleared...")
    assert password_field.get_attribute('value') == "", "Password field is not cleared"
    logger.info("Password field is cleared!")

