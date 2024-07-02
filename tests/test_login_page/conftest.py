import ssl
import pytest
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options

ssl._create_default_https_context = ssl._create_unverified_context

# CONSTANTS
LOGIN_PAGE = 'https://phptravels.net/login'
DASHBOARD_PAGE = 'https://phptravels.net/dashboard'

@pytest.fixture
def driver():
    chromedriver_autoinstaller.install()

    # Set up chrome options for headless mode
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
def login_url():
    return LOGIN_PAGE

@pytest.fixture
def dashboard_url():
    return DASHBOARD_PAGE