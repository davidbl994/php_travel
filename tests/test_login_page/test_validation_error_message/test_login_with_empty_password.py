from utils.config import USERNAME, EMPTY_PASSWORD

def test_logout_user(driver, login_page, search_url):
    login_page.insert_email(USERNAME)
    login_page.insert_password(EMPTY_PASSWORD)
    login_page.select_remember_me()
    login_page.click_login_btn()

    login_page.get_error_message(driver)