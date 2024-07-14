import pytest

@pytest.mark.usefixtures("driver", "login_page")
def test_load_login_page(driver, login_page):
    """
    Test to verify that the login page has the correct title.
    """
    # Verify that the login page has the correct title
    print("Checking that the login page has the correct title...")
    login_page.confirm_login_title()
    print("Login page has the correct title!")