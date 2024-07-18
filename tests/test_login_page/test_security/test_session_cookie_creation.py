from pages.dashboard_page import DashboardPage
from utils.config import USERNAME, PASSWORD

def test_session_cookie_creation(driver, login_page):

    login_page.insert_email(USERNAME)
    login_page.insert_password(PASSWORD)
    login_page.click_login_btn()

    dashboard_page = DashboardPage(driver)
    dashboard_page.welcome_back_msg()

    dashboard_page.cookie_session_confirm()