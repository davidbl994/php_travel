# Verify that the placeholder texts for username and password fields are correct.
import pytest
@pytest.mark.usefixtures("driver", "login_page")
def test_load_login_page(driver, login_page):
    """
    Test to verify that the placeholder texts for username and password fields are correct.
    """
    # Verify placeholder texts
    print("Checking that the placeholder texts for username and password fields are correct...")
    login_page.correct_placeholders()
    print("Placeholder texts for username and password fields are correct!")