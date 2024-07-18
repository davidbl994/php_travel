from selenium.webdriver.common.by import By
from pages.login_page import logger

def test_password_field_encryption(driver, login_page):

    password_field_locator = driver.find_element(By.NAME, 'password')
    logger.info("Checking is password securely stored in the browser...")
    assert password_field_locator.get_attribute("type") == "password", "Password is not stored securely in the browser"
    logger.info("Password is securely stored in the browser!")
