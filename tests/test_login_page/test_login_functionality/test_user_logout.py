from pages.dashboard_page import DashboardPage
from pages.search_page import SearchPage
from utils.config import USERNAME, PASSWORD

def test_logout_user(driver, login_page, search_url):

    login_page.login(USERNAME, PASSWORD)
    login_page.click_login_btn()

    dashboard_page = DashboardPage(driver)

    dashboard_page.click_on_account()
    dashboard_page.click_on_logout()

    search_page = SearchPage(driver)
    assert driver.current_url == search_url, f"Failed to navigate to the login page. Current URL: {driver.current_url}"

    print("User successfully logged out and navigated to the login page.")