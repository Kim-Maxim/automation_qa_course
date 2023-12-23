import random
import pytest
import allure

from pages.elements_page import *


@allure.severity(allure.severity_level.BLOCKER)
@allure.parent_suite("Tools")
@allure.suite("Elements")
class TestElements:
    @allure.sub_suite("TextBox")
    class TestTextBox:
        @pytest.mark.smoke
        @allure.title("Check TextBox")
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            (
                full_name,
                email,
                current_address,
                permanent_address,
            ) = text_box_page.fill_all_fields()
            (
                output_name,
                output_email,
                output_current_address,
                output_permanent_address,
            ) = text_box_page.check_filled_form()
            assert full_name == output_name, "the full_name does not match"
            assert email == output_email, "the email does not match"
            assert (
                current_address == output_current_address
            ), "the current_address does not match"
            assert (
                permanent_address == output_permanent_address
            ), "the permanent_address does not match"

    @allure.sub_suite("CheckBox")
    class TestCheckBox:
        @pytest.mark.smoke
        @allure.title("Check CheckBox")
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, "checkboxes have not been selected"

    @allure.sub_suite("RadioButton")
    class TestRadioButton:
        @allure.title("Check RadioButton")
        @pytest.mark.smoke
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(
                driver, "https://demoqa.com/radio-button"
            )
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button("yes")
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button("impressive")
            output_impressive = radio_button_page.get_output_result()
            # radio_button_page.click_on_the_radio_button('no')
            # output_no = radio_button_page.get_output_result()
            assert output_yes == "Yes", "'Yes' have not been selected"
            assert (
                output_impressive == "Impressive"
            ), "'Impressive' have not been selected"
            # assert output_no == 'No', "'No' have not been selected"

    @allure.sub_suite("WebTable")
    class TestWebTable:
        @pytest.mark.smoke
        @allure.title("Сheck to add a person to the table")
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            assert new_person in table_result, "New person was not in the table result"

        @pytest.mark.smoke
        @allure.title("Check human search in table")
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result, "Key word was not in the table result"

        @pytest.mark.smoke
        @allure.title("Checking to update the persons info in the table")
        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, "the person card has not been changed"

        @pytest.mark.smoke
        @allure.title("Checking to remove a person from the table")
        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == "No rows found"

        @pytest.mark.smoke
        @allure.title("Check the change in the number of rows in the table")
        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [
                5,
                10,
                20,
            ], "The number of rows in the table has not been changed incorrectly"

    @allure.sub_suite("Buttons page")
    class TestButtonPage:
        @pytest.mark.smoke
        @allure.title("Checking clicks of different types")
        def test_different_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            double = button_page.click_on_different_button("double")
            right = button_page.click_on_different_button("right")
            click = button_page.click_on_different_button("click")
            assert (
                double == "You have done a double click"
            ), "The double click button was not presed"
            assert (
                right == "You have done a right click"
            ), "The right click button was not presed"
            assert (
                click == "You have done a dynamic click"
            ), "The dynamic click button was not presed"

    @allure.sub_suite("Links page")
    class TestLinksPage:
        @pytest.mark.smoke
        @allure.title("Checking the link")
        def test_check_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url, "the link is broken or url is incorrect"

        @pytest.mark.smoke
        @allure.title("Checking the broken link")
        def test_broken_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            responce_code = links_page.check_broken_link(
                "https://demoqa.com/bad-request"
            )
            assert responce_code == 400, "the link works or statuscode in 400"

    @allure.sub_suite("Upload and Download page")
    class TestUploadAndDownload:
        @pytest.mark.smoke
        @allure.title("Check upload file")
        def test_upload_file(self, driver):
            upload_and_download_page = UploadAndDownloadPage(
                driver, "https://demoqa.com/upload-download"
            )
            upload_and_download_page.open()
            file_name, result = upload_and_download_page.upload_file()
            assert file_name == result, "the file has not been uploaded"

        @pytest.mark.smoke
        @allure.title("Check download file")
        def test_download_file(self, driver):
            upload_and_download_page = UploadAndDownloadPage(
                driver, "https://demoqa.com/upload-download"
            )
            upload_and_download_page.open()
            check = upload_and_download_page.download_file()
            assert check is True, "the file has not been downloaded"

    @allure.sub_suite("Dynamic properties page")
    class TestDynamicPropertiesPage:
        @pytest.mark.smoke
        @allure.title("Check dynamic properties")
        def test_enable_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(
                driver, "https://demoqa.com/dynamic-properties"
            )
            dynamic_properties_page.open()
            enable = dynamic_properties_page.check_enable_button()
            assert enable is True, "button did not enable after 5 second"

        @pytest.mark.smoke
        @allure.title("Check appear button")
        def test_color_change(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(
                driver, "https://demoqa.com/dynamic-properties"
            )
            dynamic_properties_page.open()
            color_before, color_after = dynamic_properties_page.check_changed_of_color()
            assert color_before == color_after, "colors have not been changed"

        @pytest.mark.smoke
        @allure.title("Check enable button")
        def test_visible_after(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(
                driver, "https://demoqa.com/dynamic-properties"
            )
            dynamic_properties_page.open()
            appear = dynamic_properties_page.check_apear_of_button()
            assert appear is True, "button did not appear after 5 second"
