import pytest
from pages.login_page import logger
from utils.config import PASSWORD
from utils.locators import Login

@pytest.mark.usefixtures("driver")
def test_input_fields_cleared_on_refresh(driver, login_page):

    logger.info("Inserting a password...")
    login_page.insert_password(PASSWORD)
    logger.info("Password inserted!")

    password_field = driver.find_element(*Login.PASSWORD)
    logger.info("Checking the expected input...")
    assert password_field.get_attribute('value') == PASSWORD, "Password field does not contain the expected input"
    logger.info("Password field contains the expected input!")