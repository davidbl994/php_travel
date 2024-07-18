import json
import time
from pages.login_page import logger

def test_login_page_load_time(driver, login_url):

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