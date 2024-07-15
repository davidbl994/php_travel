import logging
import os
import time
from PIL import Image, ImageChops
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import Login
from axe_selenium_python import Axe

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.baseline_dir = "baselines/"
        self.diff_dir = "diffs/"
        os.makedirs(self.baseline_dir, exist_ok=True)
        os.makedirs(self.baseline_dir, exist_ok=True)

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def open_login_page(self, url):
        try:
            self.driver.get(url)
            logger.info("Login page opened successfully.")
            return True
        except Exception as e:
            logger.error(f"Failed to open the login page {e}")
            return False

    def get_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def is_smartphone_img_displayed(self):
        return self.driver.find_element(*Login.SMARTPHONE_IMAGE).is_displayed()

    def insert_email(self, username):
        email = self.driver.find_element(*Login.EMAIL_ADDRESS)
        email.clear()
        email.send_keys(username)

    def insert_wrong_email(self, username):
        email = self.driver.find_element(Login.EMAIL_ADDRESS)
        email.clear()
        email.send_keys(username)

    def insert_password(self, password):
        password_field = self.driver.find_element(*Login.PASSWORD)
        password_field.clear()
        password_field.send_keys(password)

    def insert_wrong_password(self):
        password = self.driver.find_element(*Login.PASSWORD)
        password.send_keys("notdemouser")

    def login(self, username, password):
        self.insert_email(username)
        self.insert_password(password)

    def select_remember_me(self):
        remember_chck_box = self.driver.find_element(*Login.REMEMBER_CHECK_BOX)
        remember_chck_box.click()

    def click_login_btn(self):
        login_btn = self.driver.find_element(*Login.LOGIN_BTN)
        login_btn.click()

    def login_form_confirm(self):
        login_form = self.driver.find_element(*Login.LOGIN_FORM)
        return login_form.is_displayed()

    def confirm_login_title(self):
        try:
            login_title = self.driver.title  # Get the page title directly
            assert 'Login' in login_title, f"'Login' not found in page title: {login_title}"
            logger.info('Login title exists!')
        except Exception as e:
            logger.error('Login title is missing:', e)

    def get_email_placeholder(self):
        email_field = self.get_element(Login.EMAIL_ADDRESS)
        return email_field.get_attribute("placeholder")

    def get_password_placeholder(self):
        password_field = self.get_element(Login.PASSWORD)
        return password_field.get_attribute("placeholder")

    def correct_placeholders(self):
        username_placeholder = self.get_email_placeholder()
        password_placeholder = self.get_password_placeholder()

        # Define the expected placeholder texts
        expected_username_placeholder = "name@example.com"
        expected_password_placeholder = "******"

        assert username_placeholder == expected_username_placeholder, f"Expected placeholder for username: '{expected_username_placeholder}', but got: '{username_placeholder}'"
        assert password_placeholder == expected_password_placeholder, f"Expected placeholder for password: '{expected_password_placeholder}', but got: '{password_placeholder}'"

    def is_login_button_enabled(self):
        login_button = self.get_element(Login.LOGIN_BTN)
        return login_button.is_enabled()

    def is_remember_me_box_selected(self):
        remember_me = self.get_element(Login.REMEMBER_CHECK_BOX)
        return remember_me.is_selected()

    def take_screenshot(self, file_path):
        self.driver.save_screenshot(file_path)

    # Function to compare images
    def compare_images(img1_path, img2_path, diff_path):
        img1 = Image.open(img1_path)
        img2 = Image.open(img2_path)
        diff = ImageChops.difference(img1, img2)

        if diff.getbbox():
            diff.save(diff_path)
            return False
        return True

    def get_pop_up_warning(self):
        try:
            # Wait for the alert to be present
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            logger.info("Uključite znak "@" u e-adresu.", alert.text)
            alert.accept()
        except:
            logger.info("No alert present")

    def get_error_message(self, driver):
        time.sleep(0.5)
        error_message = driver.find_element(*Login.INVALID_LOGIN_POP_UP).text
        assert "Invalid Login" in error_message, "Error message not found"

    def insert_sql_string(self, driver):
        # SQL injection strings
        sql_injection_username = "' OR '1'='1"
        sql_injection_password = "' OR '1'='1"

        email_field = self.get_element(Login.EMAIL_ADDRESS)
        password_field = self.get_element(Login.PASSWORD)
        login_button = self.get_element(Login.LOGIN_BTN)

        email_field.send_keys(sql_injection_username)
        password_field.send_keys(sql_injection_password)
        login_button.click()

        try:
            # Wait for the error message to appear
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Login.INVALID_LOGIN_POP_UP))
            error_message = driver.find_element(Login.INVALID_LOGIN_POP_UP)
            assert "Invalid Login" in error_message.text, "Login should fail with SQL injection attempt"
        except Exception as e:
            assert False, f"SQL injection test failed: {e}"

    def insert_xss_payloads(self, driver):
        # xss payloads
        xss_payload = "<script>alert('XSS')</script>"

        email_field = self.get_element(Login.EMAIL_ADDRESS)
        password_field = self.get_element(Login.PASSWORD)
        login_btn = self.get_element(Login.LOGIN_BTN)

        email_field.send_keys(xss_payload)
        password_field.send_keys(xss_payload)
        login_btn.click

    def submit_forged_request(self, username, password):
        # Bypass normal form submission to simulate CSRF attack
        script = f"""
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "{self.driver.current_url}", true);
        xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        xhr.send("email={username}&password={password}");"""
        self.driver.execute_script(script)

    def run_axe_accessibility_checks(self):
        axe = Axe(self.driver)
        axe.inject()
        results = axe.run()
        axe.write_results(results, 'axe-results-screen-reader.json')
        return results