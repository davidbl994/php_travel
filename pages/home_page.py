from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import Demo

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def open_home_page(self, url):
        try:
            self.driver.get(url)
            return True
        except Exception as e:
            print(f"Failed to open the home page: {e}")
            return False

    def is_php_travels_logo_displayed(self):
        php_logo_element = self.driver.find_element(*Demo.PHP_TRAVEL_LOGO)
        return php_logo_element.is_dislplayed()

    def get_header_text(self):
        header_element = self.driver.find_element(*Demo.DEMONSTRATION_HEADER)
        return header_element.text