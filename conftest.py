import pytest
import allure

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope = 'function')
def driver():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()