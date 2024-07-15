import time
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import logger
from utils.config import USERNAME, PASSWORD

def test_login_response_time(driver, login_page, dashboard_url):
    """
    Test to measure the response time of a successful login attempt and ensure it is within acceptable limits.

    Args:
        driver (WebDriver): The Selenium WebDriver instance.
        login_url (str): The URL of the login page.
        dashboard_url (str): The URL of the dashboard page, indicating successful login.
    """

    login_page.insert_email(USERNAME)
    login_page.insert_password(PASSWORD)

    start_time = time.time()
    login_page.click_login_btn()

    try:
        WebDriverWait(driver, 10).until(EC.url_contains(dashboard_url))
        end_time = time.time()
        login_response_time = end_time - start_time
        logger.info(f"Login response time: {login_response_time:.2f} seconds")

        # Log performance entries
        logs = driver.get_log("performance")
        for entry in logs:
            log = json.loads(entry["message"])["message"]
            if log["method"] == "Network.responseReceived" and log["params"]["response"]["url"].startswith(
                    dashboard_url):
                logger.info(f"Response received at {log['params']['timestamp']}")

        acceptable_response_time = 3.0
        assert login_response_time <= acceptable_response_time, \
            f"Login response time is too high: {login_response_time:.2f} seconds"
    except Exception as e:
        logger.error(f"Login failed: {e}")
        assert False, f"Login failed due to: {e}"