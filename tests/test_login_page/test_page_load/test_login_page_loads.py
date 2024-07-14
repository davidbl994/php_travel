# Verify that the login page loads successfully
import pytest
@pytest.mark.usefixtures("driver", "login_url")
def test_load_login_page(driver, login_page):
    """
    Test that the login page loads successfully and confirms the presence of the login form.
    """
    # Check that the login form is present
    print("Checking that the login form is present...")
    assert login_page.login_form_confirm(), "Failed to confirm the login form is present"
    print("Login form is successfully loaded!")
