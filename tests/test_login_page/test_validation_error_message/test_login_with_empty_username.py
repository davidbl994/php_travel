from pages.login_page import logger
from utils.config import EMPTY_USERNAME, PASSWORD

def test_logout_user(driver, login_page, search_url):
    logger.info("Inserting mail...")
    login_page.insert_email(EMPTY_USERNAME)
    logger.info("Inserting password...")
    login_page.insert_password(PASSWORD)
    logger.info("Selecting remember me checkbox...")
    login_page.select_remember_me()
    logger.info("Clicking login button...")
    login_page.click_login_btn()

    login_page.get_error_message(driver)
