import ssl
import pytest
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options

ssl.create_default_https_context = ssl.create_unverified_context

# CONSTANTS

HOME_PAGE = 'https://phptravels.com/demo/'
LOGIN_PAGE = 'https://phptravels.net/login'

@pytest.fixture
def driver():
    chromedriver_autoinstaller.install()

    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # Create the Webdriver with the specified
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)

    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture
def home_url():
    return HOME_PAGE

@pytest.fixture
def login_url():
    return LOGIN_PAGE