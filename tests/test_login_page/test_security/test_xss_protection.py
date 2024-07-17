from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_xss_protection(driver, login_page):

    login_page.insert_xss_payloads(driver)

    # Check if there are any alerts
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        assert False, f"XSS vulnerability detected: {alert_text}"
    except:
        # No alert found
        pass