import allure
import pytest

from pages.form_page import FormPage


@allure.severity(allure.severity_level.BLOCKER)
@allure.parent_suite("Tools")
@allure.suite("Forms")
class TestForm:
    @allure.sub_suite("FormPage")
    class TestFormPage:
        @pytest.mark.smoke
        @allure.title("Check form")
        def test_form(self, driver):
            form_page = FormPage(driver, "https://demoqa.com/automation-practice-form")
            form_page.open()
            driver.execute_script("document.body.style.zoom='90%'")
            p = form_page.fill_form_fields()
            result = form_page.form_result()
            assert [p.firstname + " " + p.lastname, p.email] == [
                result[0],
                result[1],
            ], "the form has not been filled"
