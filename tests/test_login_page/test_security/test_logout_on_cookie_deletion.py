from pages.login_page import logger
from pages.dashboard_page import DashboardPage
from utils.config import USERNAME, PASSWORD

def test_session_cookie_creation(driver, login_page, login_url):

    logger.info("Inserting email...")
    login_page.insert_email(USERNAME)
    logger.info("Email inserted")

    login_page.insert_password(PASSWORD)
    logger.info("Password inserted")

    logger.info("Clicking login button...")
    login_page.click_login_btn()
    logger.info("Login button clicked")

    logger.info("Opening Dashboard page...")
    dashboard_page = DashboardPage(driver)
    logger.info("Dashboard page opened")
    dashboard_page.welcome_back_msg()

    logger.info("Deleting cookie...")
    driver.delete_cookie("PHPSESSID")
    logger.info("Cookie deleted")

    logger.info("Refreshing web page...")
    driver.refresh()

    logger.info("Asserting current url vs login_url")
    assert driver.current_url == login_url, "User is not redirected to the login page after session cookie is deleted."
    logger.info("The user is redirected to the login page.")