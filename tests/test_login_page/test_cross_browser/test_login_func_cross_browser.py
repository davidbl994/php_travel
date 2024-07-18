from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import USERNAME, PASSWORD

def test_login_functionality(driver, login_url, dashboard_url):

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    login_page.open_login_page(login_url)
    assert driver.current_url == login_url, "Failed to navigate to the login page"

    login_page.insert_email(USERNAME)
    login_page.insert_password(PASSWORD)
    login_page.click_login_btn()

    dashboard_page.open_dashboard_page(dashboard_url)
    assert dashboard_page.is_logged_in(), "Login failed!"