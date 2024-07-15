from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.login_page import logger
from utils.config import USERNAME, PASSWORD

def test_login_functionality(driver, login_url, dashboard_url):
    """
    Test to verify login functionality across different browsers.

    Args:
        driver (WebDriver): The Selenium WebDriver instance.
        login_url (str): The URL of the login page.
        dashboard_url (str): The URL of the dashboard page, indicating successful login.
    """
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    logger.info("Opening login page...")
    login_page.open_login_page(login_url)
    assert driver.current_url == login_url, "Failed to navigate to the login page"

    logger.info("Inserting email...")
    login_page.insert_email(USERNAME)
    logger.info("Inserting password...")
    login_page.insert_password(PASSWORD)
    logger.info("Clicking login button...")
    login_page.click_login_btn()

    logger.info("Verifying that we are logged in...")
    dashboard_page.open_dashboard_page(dashboard_url)
    assert dashboard_page.is_logged_in(), "Login failed!"