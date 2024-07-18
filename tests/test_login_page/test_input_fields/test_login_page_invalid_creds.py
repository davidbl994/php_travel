import pytest
from utils.config import INVALID_USERNAME, INVALID_PASSWORD

@pytest.mark.usefixtures("driver")
def test_login_invalid_creds(driver, login_page):

    login_page.insert_wrong_email(INVALID_USERNAME)
    login_page.insert_wrong_password(INVALID_PASSWORD)
    login_page.click_login_btn()

    login_page.get_error_message(driver)
    print("Invalid login!")