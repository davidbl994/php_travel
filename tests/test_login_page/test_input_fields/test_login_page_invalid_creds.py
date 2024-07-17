import pytest
from pages.login_page import logger
from utils.config import INVALID_USERNAME, INVALID_PASSWORD

@pytest.mark.usefixtures("driver")
def test_login_invalid_creds(driver, login_page):

    logger.info("Inserting wrong mail...")
    login_page.insert_wrong_email(INVALID_USERNAME)
    logger.info("Inserting wrong password...")
    login_page.insert_wrong_password(INVALID_PASSWORD)
    logger.info("Clicking login button...")
    login_page.click_login_btn()
    logger.info("Login button clicked")

    login_page.get_error_message(driver)
    logger.info("Invalid login")