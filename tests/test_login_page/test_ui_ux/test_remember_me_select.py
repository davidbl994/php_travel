import pytest
from pages.login_page import logger

@pytest.mark.usefixtures("driver", "login_page")
def test_load_login_page(driver, login_page):
    """
    Test to verify that the 'Remember me' checkbox is selectable and remains selected.
    """
    logger.info("Clicking on the checkbox 'Remember me'...")
    login_page.select_remember_me()

    logger.info("Checking that the checkbox is selected...")
    assert login_page.is_remember_me_box_selected(), "Checkbox should be selected after clicking on it"
    logger.info("Checkbox 'Remember me' is selected!")