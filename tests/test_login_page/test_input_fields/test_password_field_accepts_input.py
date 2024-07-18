import pytest
from utils.config import PASSWORD
from utils.locators import Login

@pytest.mark.usefixtures("driver")
def test_input_fields_cleared_on_refresh(driver, login_page):

    login_page.insert_password(PASSWORD)

    password_field = driver.find_element(*Login.PASSWORD)
    print("Checking the expected input...")
    assert password_field.get_attribute('value') == PASSWORD, "Password field does not contain the expected input"
    print("Password field contains the expected input!")