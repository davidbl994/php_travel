# Verify that the checkbox Remember me is selected
import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("driver", "login_url")
def test_load_login_page(driver, login_url):
    login_page = LoginPage(driver)
    print("Opening login page...")
    login_page.open_login_page(login_url)

    # Click on the checkbox Remember me
    print("Clicking on the checkbox 'Remember me'...")
    #login_page.select_remember_me()

    # Check that the checkbox Remember me is selected
    print("Checking that the checkbox is selected...")
    assert login_page.is_remember_me_box_selected(), "Checkbox should be selected once it is clicked on it"
    print("Checkbox Remember me is selected!")
