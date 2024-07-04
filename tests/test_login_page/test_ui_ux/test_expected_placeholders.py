import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("driver", "login_url")
def test_load_login_page(driver, login_url):
    login_page = LoginPage(driver)
    print("Opening login page...")
    login_page.open_login_page(login_url)

    print("Checking that the placeholder texts for username and password fields are correct...")
    login_page.correct_placeholders()
    print("Placeholder texts for username and password fields are correct!")