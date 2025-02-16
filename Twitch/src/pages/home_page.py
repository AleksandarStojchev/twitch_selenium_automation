from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self,driver):
            super().__init__(driver)

    URL = "https://www.twitch.tv/"
    search_button = (By.XPATH, "//input[@type='search']")
    search_input =  (By.XPATH, "//input[@placeholder='Search']")
    browse_button = (By.XPATH, "//div[normalize-space(text())='Browse']/parent::div")
