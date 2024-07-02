import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("driver", "login_url")
def test_load_login_page(driver, login_url):
    login_page = LoginPage(driver)
    print("Opening login page...")
    login_page.open_login_page(login_url)

    # Verify that the login page has the correct title
    print("Checking that the login page has the correct title...")
    login_page.confirm_login_title()
    print("Login page has the correct title!")