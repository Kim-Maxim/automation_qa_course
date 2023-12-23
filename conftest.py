import pytest
import allure

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--log-level=1")
    # chrome_options.set_capability("browserVersion", "118")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.page_load_strategy = "eager"
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(
        attach,
        name=f"Screenshot {datetime.today()}",
        attachment_type=allure.attachment_type.PNG,
    )
    driver.quit()
