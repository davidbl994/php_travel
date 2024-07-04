# Verify that the login button is enabled when the page loads.
import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("driver", "login_url")
def test_load_login_page(driver, login_url):
    login_page = LoginPage(driver)
    print("Opening login page...")
    login_page.open_login_page(login_url)

    # Check that the login button is enabled
    assert login_page.is_login_button_enabled(), "Login button should be enabled when the page loads"