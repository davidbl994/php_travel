import json
import time
import logging

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def test_login_page_load_time(driver, login_url):
    """
    Test to measure the load time of the login page and ensure it is within acceptable limits.

    Args:
        driver (WebDriver): The Selenium WebDriver instance.
        login_url (str): The URL of the login page.
    """
    start_time = time.time()
    driver.get(login_url)
    end_time = time.time()

    page_load_time = end_time - start_time
    logger.info(f"Page load time: {page_load_time:.2f} seconds")

    # Log performance entries
    logs = driver.get_log("performance")
    for entry in logs:
        log = json.loads(entry["message"])["message"]
        if log["method"] == "Network.responseReceived" and log["params"]["response"]["url"] == login_url:
            logger.info(f"Response received at {log['params']['timestamp']}")

    # Set an acceptable threshold for page load time
    acceptable_load_time = 5.0
    assert page_load_time <= acceptable_load_time, \
        f"Page load time is high: {page_load_time:.2f} seconds"
