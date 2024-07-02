import pytest
from pages.home_page import HomePage

def test_home_page(driver, home_url):
    home_page = HomePage(driver)
    print("Opening home page...")
    assert home_page.open_home_page(home_url), "Failed to open the home page"
    assert home_page.driver.current_url == home_url, "Failed to navigate to the home page"

    # Confirm the presence of PHP Travels logo
    print("Confirming the presence of PHP Travels logo...")
    assert home_page.is_php_travels_logo_displayed(), "Failed to confirm the PHP Travels logo"