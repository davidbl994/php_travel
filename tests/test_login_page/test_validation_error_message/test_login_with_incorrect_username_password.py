
from utils.config import INVALID_USERNAME, INVALID_PASSWORD

def test_logout_user(driver, login_page, search_url):
    login_page.insert_email(INVALID_USERNAME)
    login_page.insert_password(INVALID_PASSWORD)
    login_page.select_remember_me()
    login_page.click_login_btn()

    login_page.get_error_message(driver)