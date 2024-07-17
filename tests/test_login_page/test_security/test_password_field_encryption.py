from selenium.webdriver.common.by import By

def test_password_field_encryption(driver, login_page):

    password_field_locator = driver.find_element(By.NAME, 'password')
    assert password_field_locator.get_attribute("type") == "password", "Password is not stored securely in the browser"
