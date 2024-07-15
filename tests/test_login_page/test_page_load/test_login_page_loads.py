import pytest
from pages.login_page import logger
@pytest.mark.usefixtures("driver", "login_page")
def test_load_login_page(driver, login_page):
    """
    Test that the login page loads successfully and confirms the presence of the login form.
    """
    logger.info("Checking that the login form is present...")
    assert login_page.login_form_confirm(), "Login form is not present on the login page."
    logger.info("Login form is successfully loaded!")
