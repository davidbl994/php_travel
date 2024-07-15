import pytest
from pages.login_page import logger

@pytest.mark.usefixtures("driver", "login_page")
def test_load_login_page(driver, login_page):
    """
    Test to verify that the login button is enabled when the login page loads.
    """
    logger.info("Verifying that the login button is enabled...")
    assert login_page.is_login_button_enabled(), "Login button should be enabled when the page loads"
    logger.info("Login button is enabled!")