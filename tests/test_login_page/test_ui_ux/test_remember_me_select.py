# Verify that the checkbox Remember me is selected
import pytest

@pytest.mark.usefixtures("driver", "login_page")
def test_load_login_page(driver, login_page):
    """
    Test to verify that the 'Remember me' checkbox is selectable and remains selected.
    """
    # Click on the checkbox 'Remember me'
    print("Clicking on the checkbox 'Remember me'...")
    login_page.select_remember_me()

    # Check that the checkbox 'Remember me' is selected
    print("Checking that the checkbox is selected...")
    assert login_page.is_remember_me_box_selected(), "Checkbox should be selected after clicking on it"
    print("Checkbox 'Remember me' is selected!")