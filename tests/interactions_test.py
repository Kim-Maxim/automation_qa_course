import pytest
import allure

from pages.interactions_page import ResizablePage, SelectablePage, SortablePage

@allure.suite('Interactions')
class TestInteractions:

    @allure.feature('Sortable Page')
    class TestSortablePage:
        
        @allure.title('Check changed sortable list and grid')
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after, "The order of the list has not been changed"
            assert grid_before != grid_after, "The order of the list has not been changed"

    @allure.feature('Selectable Page')
    class TestSelectablePage:

        @allure.title('Check changed selectable list and grid')
        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            item_list = selectable_page.selected_list_item()
            item_grid = selectable_page.selected_grid_item()
            assert len(item_list) > 0, "No elements were selected"
            assert len(item_grid) > 0, "No elements were selected"

    @allure.feature('Resizable Page')
    class TestRssizablePage:
        @allure.title('Check changed resizable boxes')
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_box, min_box = resizable_page.change_size_resizable_box()
            max_resize, min_resize = resizable_page.change_size_resizable()
            assert max_box == ('width: 500px; height: 300px;', 'width: 500px; height: 300px;'), "It is not OK"
            assert min_box == ('width: 150px; height: 150px;', 'width: 150px; height: 150px;'), "It is not OK"
            print(max_resize)
            print(min_resize)
            