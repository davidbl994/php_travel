import pytest
from pages.login_page import logger
@pytest.mark.usefixtures("driver", "login_page")
def test_load_login_page(driver, login_page):
    """
    Test to verify that the placeholder texts for username and password fields are correct.
    """
    logger.info("Checking that the placeholder texts for username and password fields are correct...")
    login_page.correct_placeholders()
    logger.info("Placeholder texts for username and password fields are correct!")