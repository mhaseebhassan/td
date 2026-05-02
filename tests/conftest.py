import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="session")
def base_url():
    return "http://localhost:5000"

@pytest.fixture(scope="session")
def test_user():
    return "testuser_selenium"

@pytest.fixture(scope="session")
def test_pass():
    return "seleniumpass123"

@pytest.fixture(scope="session")
def driver():
    """Create a headless Chrome WebDriver for the entire test session."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    d = webdriver.Chrome(options=chrome_options)
    d.implicitly_wait(5)
    yield d
    d.quit()

@pytest.fixture(scope="session")
def wait_for():
    def _wait(driver, by, value, timeout=10):
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
    return _wait

@pytest.fixture(scope="session")
def wait_clickable():
    def _wait(driver, by, value, timeout=10):
        return WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
    return _wait
