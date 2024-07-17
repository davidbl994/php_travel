import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.login_page import logger
from utils.config import USERNAME, PASSWORD

@pytest.mark.xfail
def test_remember_me_functionality(driver, login_page, login_url, dashboard_url):

    logger.info("Inserting mail...")
    login_page.insert_email(USERNAME)
    logger.info("Inserting password...")
    login_page.insert_password(PASSWORD)
    logger.info("Selecting remember me checkbox...")
    login_page.select_remember_me()
    logger.info("Clicking login button...")
    login_page.click_login_btn()

    logger.info("Verifying that we are logged in...")
    cookies = driver.get_cookies()

    dashboard_page = DashboardPage(driver)
    assert dashboard_page.open_dashboard_page(dashboard_url)
    assert dashboard_page.is_logged_in(), "Login failed with 'Remember Me' selected."

    cookies = driver.get_cookies()
    driver.quit()

    login_page = LoginPage(driver)
    login_page.open_login_page(login_url)

    for cookie in cookies:
        if 'domain' not in cookie:
            cookie['domain'] = 'phptravels.net'
        driver.add_cookie(cookie)
    driver.refresh()

    logger.info("Verifying that we are still logged in...")
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_logged_in(), "User was not remembered after closing and reopening the browser!"