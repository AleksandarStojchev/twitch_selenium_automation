from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest:
    def setup_method(self):
        chrome_options = webdriver.ChromeOptions()
        mobile_emulation = {"deviceName": "iPhone X"}
        chrome_options.add_argument('window-size=375x812')
        chrome_options.add_argument("--disable-notifications")

        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.twitch.tv/")
        self.accept_cookies()

    def accept_cookies(self):
        accept_cookies = (By.XPATH,"//button//div[normalize-space(text())='Accept']")
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(accept_cookies)).click()


    def teardown_method(self):
        self.driver.quit()

