from selenium.webdriver.common.by import By

class Demo:
    LOGIN_BTN = (By.CSS_SELECTOR, '#mynavbar a.login-button')
    SIGNUP_BTN = (By.CSS_SELECTOR, '#mnavbar a.signup-button')
    WHATSUP = (By.CSS_SELECTOR, 'a.some-class > div > svg')
    DEMONSTRATION_HEADER = (By.CSS_SELECTOR, '#swup h1')
    FIRST_NAME = (By.CSS_SELECTOR, '#swup input[name="unique-name"]')
    LAST_NAME = (By.CSS_SELECTOR, '#swup input.last-name')
    BUSINESS_NAME = (By.CSS_SELECTOR, '#swup input.business-name')
    EMAIL = (By.CSS_SELECTOR, '#swup input.email')
    SUBMIT_BTN = (By.CSS_SELECTOR, '.btn.btn-primary.btn-lg.w-100')
    RESULT = (By.CSS_SELECTOR, 'input.form-control.w-100[type="text"]')
    DEMO_IMAGE = (By.CSS_SELECTOR, 'img[src="https://phptravels.com/assets/img/screen2.png"]')
    CHAT_NOW = (By.CSS_SELECTOR,)