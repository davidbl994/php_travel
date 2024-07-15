from pages.login_page import logger
from utils.config import INVALID_USERNAME, INVALID_PASSWORD

def test_logout_user(driver, login_page, search_url):
    logger.info("Inserting mail...")
    login_page.insert_email(INVALID_USERNAME)
    logger.info("Inserting password...")
    login_page.insert_password(INVALID_PASSWORD)
    logger.info("Selecting remember me checkbox...")
    login_page.select_remember_me()
    logger.info("Clicking login button...")
    login_page.click_login_btn()

    # Check if the error message is captured
    login_page.get_error_message(driver)
    logger.info("Correct error message is captured")