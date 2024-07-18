import pytest
@pytest.mark.usefixtures("driver", "login_page")
def test_load_login_page(driver, login_page):

    assert login_page.login_form_confirm(), "Login form is not present on the login page."