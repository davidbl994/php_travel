from utils.config import EMPTY_USERNAME, PASSWORD

def test_logout_user(driver, login_page, search_url):
    login_page.insert_email(EMPTY_USERNAME)
    login_page.insert_password(PASSWORD)
    login_page.select_remember_me()
    login_page.click_login_btn()

    login_page.get_error_message(driver)