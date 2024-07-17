from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.dashboard_page import DashboardPage
from pages.login_page import logger
from utils.locators import Dashboard
from utils.config import USERNAME, PASSWORD

def test_login_page(driver, login_page):

    logger.info("Inserting mail...")
    login_page.insert_email(USERNAME)
    logger.info("Inserting password...")
    login_page.insert_password(PASSWORD)
    logger.info("Selecting remember me checkbox...")
    login_page.select_remember_me()
    logger.info("Clicking login button...")
    login_page.click_login_btn()

    dashboard_page = DashboardPage(driver)

    welcome_back_msg_locator = By.XPATH
    welcome_back_msg_value = Dashboard.WELCOME_BACK_MSG[1]
    welcome_back_msg = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((welcome_back_msg_locator, welcome_back_msg_value))
    )
    logger.info("Redirected to Dashboard page")

    assert dashboard_page.welcome_back_msg()

    logger.info("Dashboard message: Welcome Back User!")