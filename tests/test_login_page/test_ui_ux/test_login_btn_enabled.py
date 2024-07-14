# Verify that the login button is enabled when the page loads.

import pytest

@pytest.mark.usefixtures("driver", "login_page")
def test_load_login_page(driver, login_page):
    """
    Test to verify that the login button is enabled when the login page loads.
    """
    # Verify login button is enabled
    print("Verifying that the login button is enabled...")
    assert login_page.is_login_button_enabled(), "Login button should be enabled when the page loads"
    print("Login button is enabled!")