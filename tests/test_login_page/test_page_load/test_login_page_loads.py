# Verify that the login page loads successfully
import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("driver", "login_url")
def test_load_login_page(driver, login_url):
    login_page = LoginPage(driver)
    print("Opening login page...")
    login_page.open_login_page(login_url)

    # Check that the login form is present
    print("Checking that the login form is present...")
    assert login_page.login_form_confirm(), "Failed to confirm the login form is present"
    print("Login form is successfully loaded!")
