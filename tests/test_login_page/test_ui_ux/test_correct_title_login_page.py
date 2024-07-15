import pytest
from pages.login_page import logger

@pytest.mark.usefixtures("driver", "login_page")
def test_load_login_page(driver, login_page):
    """
    Test to verify that the login page has the correct title.
    """
    logger.info("Checking that the login page has the correct title...")
    login_page.confirm_login_title()
    logger.info("Login page has the correct title!")