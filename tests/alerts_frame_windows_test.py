import pytest
import allure

from pages.alerts_frame_windows_page import AlertsPage, BrowserWindowsPage, FramesPage, ModalDialogsPage, NestedFramesPage

@allure.severity(allure.severity_level.BLOCKER)
@allure.suite('Alerts, Frame & Windows')
class TestAlertsFrameWindow:

    @allure.feature('Browser Windows')
    class TestBrowserWindows:

        @pytest.mark.smoke
        @allure.title('Checking the opening of a new tab')
        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_page.open()
            text_result = new_tab_page.check_opened_new_tab()
            assert text_result == "This is a sample page", 'The new window has not opened or an incorrect window'
        
        @pytest.mark.smoke
        @allure.title('Checking the opening of a new window')
        def test_new_window(self, driver):
            new_window_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_window_page.open()
            text_result = new_window_page.check_opened_new_window()
            assert text_result == "This is a sample page", 'The new window has not opened or an incorrect window'

    @allure.feature('Alerts Page')
    class TestAlerts:

        @pytest.mark.smoke       
        @allure.title('Checking the opening of an alert')
        def test_see_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_see_alert()
            assert alert_text == "You clicked a button", "The new window has not opened or an incorrect window"

        @pytest.mark.smoke       
        @allure.title('Checking the opening of the alert after 5 seconds')      
        def test_see_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_alert_appear_5_sec()
            assert alert_text == "This alert appeared after 5 seconds", "Allert did not show up"

        @pytest.mark.smoke
        @allure.title('Checking the opening of the alert with confirm')
        def test_confirm_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_confirm_alert()
            assert alert_text == "You selected Ok", "Allert did not show up"
        
        @pytest.mark.smoke
        @allure.title('Checking the opening of the alert with prompt')
        def test_promt_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            text, alert_text = alerts_page.check_prompt_alert()
            assert alert_text == f"You entered {text}", "Allert did not show up"

    @allure.feature('Frame Page')
    class TestFramesPage:
        
        @pytest.mark.smoke
        @allure.title('Check the page with frames')
        def test_frames(self, driver):
            frame_page = FramesPage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            result_frame1 = frame_page.check_frame('frame1')
            result_frame2 = frame_page.check_frame('frame2')
            assert result_frame1 == ['This is a sample page', '500px', '350px'], 'The frame does not exist'
            assert result_frame2 == ['This is a sample page', '100px', '100px'], 'The frame does not exist'

    @allure.feature('Nested Page')
    class TestNestedFramesPage:
        
        @pytest.mark.smoke
        @allure.title('Check the page with nested frames')
        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nested_frame_page.open()
            parent_text, child_text = nested_frame_page.check_nested_frame()
            assert parent_text == "Parent frame", "Nested frames do not exist"
            assert child_text == "Child Iframe", "Nested frames do not exist"
    
    @allure.feature('Modal Dialog Page')
    class TestModalDialogs:

        @pytest.mark.smoke     
        @allure.title('Check the page with modal dialogs')
        def test_modal_dialogs(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialogs_page.open()
            small, large = modal_dialogs_page.check_modal_dialogs()
            assert small < large, 'text from large dialog is less than text from small dialogs'
          