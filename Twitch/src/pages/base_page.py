import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def navigate_to(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        self.find_element(locator).click()

    def click_element_from_search(self, content_name):
        locator = (By.XPATH, "//div/p[normalize-space(text())='{content}'][@class='CoreText-sc-1txzju1-0 bqCGPR']"
                   .format(content =content_name))
        self.wait.until(EC.element_to_be_clickable(locator))

        self.click_element(locator)

    def click_nth_streamer(self, nth):
        nth_streamer_locator = (By.XPATH, f"//div[@class='Layout-sc-1xcs6mc-0'][{nth}]")
        self.click_element(nth_streamer_locator)

    def wait_for_page_load(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
    def take_screenshot(self):

        # Wait until the Pause button is visible
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@data-test-selector='video-player__video-layout']//button[@aria-label='Pause']")
        ))

        file_dir = os.path.join(os.getcwd(), "screenshots")
        os.makedirs(file_dir, exist_ok=True)
        file_path = os.path.join(file_dir, "streamer_screenshot.png")
        self.driver.save_screenshot(file_path)

    def scroll_up_down(self, pixels, scroll_times):
        for _ in range(scroll_times):
            self.driver.execute_script("window.scrollBy(0, arguments[0]);", pixels)

    def type_text(self,locator, text ):
        self.find_element(locator)
        self.element = self.find_element(locator)
        self.element.clear()
        self.element.send_keys(text)






