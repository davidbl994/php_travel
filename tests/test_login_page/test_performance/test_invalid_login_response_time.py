import time
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.config import INVALID_USERNAME, INVALID_PASSWORD
from pages.login_page import logger


def test_invalid_login_response_time(driver, login_page):
    """
    Test to measure the response time of an invalid login attempt and ensure it is within acceptable limits.

    Args:
        driver (WebDriver): The Selenium WebDriver instance.
        login_url (str): The URL of the login page.
    """

    login_page.insert_email(INVALID_USERNAME)
    login_page.insert_password(INVALID_PASSWORD)
    error_message_locator = (By.XPATH, "//h4[text()='Invalid Login']")

    start_time = time.time()
    login_page.click_login_btn()

    invalid_login_response_time = None

    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(error_message_locator))
        end_time = time.time()
        invalid_login_response_time = end_time - start_time
        logger.info(f"Invalid login response time: {invalid_login_response_time:.2f} seconds")

        error_message = driver.find_element(*error_message_locator).text
        assert "Invalid Login" in error_message, "Expected error message 'Invalid Login' not found."
    except Exception as e:
        logger.error(f"Error message not captured: {e}")

    logs = driver.get_log("performance")
    for entry in logs:
        log = json.loads(entry["message"])["message"]
        if log["method"] == "Network.responseReceived" and "error" in log["params"]["response"]["url"]:
            logger.info(f"Response received at {log['params']['timestamp']}")

    acceptable_response_time = 2.0
    assert invalid_login_response_time is not None and invalid_login_response_time <= acceptable_response_time, \
        f"Invalid login response time is too high: {invalid_login_response_time:.2f} seconds"