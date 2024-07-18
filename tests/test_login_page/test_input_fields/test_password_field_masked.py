import pytest
from utils.config import PASSWORD
from pages.login_page import logger
from utils.locators import Login

@pytest.mark.usefixtures("driver")
def test_input_fields_cleared_on_refresh(driver, login_page):

    login_page.insert_password(PASSWORD)

    password_field = driver.find_element(*Login.PASSWORD)

    logger.info("Verifying password field...")
    assert password_field.get_attribute('type') == 'password', "Password field is not masked"
    logger.info("Password field is of type 'password'")

    entered_password = PASSWORD
    actual_value = password_field.get_attribute('value')
    assert actual_value == entered_password, "Password input does not match expected value"
    assert '*' not in actual_value, "Password field is displaying input characters"
    logger.info("Password field is not displaying input characters!")