import time

from pages.elements_page import TextBoxPage

class TestElemets:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            text_box_page.fill_all_fields()
            output_name, output_email, output_current_adress, output_permanent_adress = text_box_page.check_filled_form()
            print(output_name)
            print(output_email)
            print(output_current_adress)
            print(output_permanent_adress)

