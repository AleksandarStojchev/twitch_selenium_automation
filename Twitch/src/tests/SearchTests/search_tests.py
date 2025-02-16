from src.pages.home_page import HomePage
from src.tests.base_test import BaseTest



class TestsSearch(BaseTest):

    def test_search_for_specific_content(self):
        search_for = "StarCraft II"
        home_page = HomePage(self.driver)

        home_page.click_element(home_page.browse_button)
        home_page.click_element(home_page.search_button)
        home_page.type_text(home_page.search_input, search_for)

        home_page.click_element_from_search(search_for)
        home_page.scroll_up_down(100,2)
        home_page.click_nth_streamer(2)

        home_page.take_screenshot()

