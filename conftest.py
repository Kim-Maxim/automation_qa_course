import pytest
import allure

from datetime import datetime
from selenium import webdriver

@pytest.fixture(scope = 'function')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()