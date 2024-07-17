from pages.dashboard_page import DashboardPage
from pages.search_page import SearchPage
from pages.login_page import logger
from utils.config import USERNAME, PASSWORD

def test_logout_user(driver, login_page, search_url):

    logger.info("Starting test: test_logout_user")

    logger.info("Inserting email and password, selecting 'remember me', and clicking login button.")
    login_page.login(USERNAME, PASSWORD)

    logger.info("Clicking login button.")
    login_page.click_login_btn()

    logger.info("Opening Dashboard page.")
    dashboard_page = DashboardPage(driver)
    logger.info("Dashboard page opened")

    logger.info("Selecting Account")
    dashboard_page.click_on_account()

    logger.info("Logging out the user from the Dashboard page.")
    dashboard_page.click_on_logout()

    search_page = SearchPage(driver)
    assert driver.current_url == search_url, f"Failed to navigate to the login page. Current URL: {driver.current_url}"

    logger.info("User successfully logged out and navigated to the login page.")