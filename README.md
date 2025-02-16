# twitch_selenium_automation

**Project Structure**

**BasePage:** Defines common browser interaction methods.

**HomePage:** Contains locators and actions specific to the Twitch home page.

**BaseTest:** Sets up and tears down the browser session for each test.

**TestsSearch:** Implements the test case for searching and interacting with streamers.


**Test running GIF**

![twitch_test_running](https://github.com/user-attachments/assets/5616cb8a-a274-447c-9e0b-f955706630d9)


**_Note_**
_Instead of using time.sleep(), I would use explicit waits (WebDriverWait). In work environment I would aks Devs for an element which loads last on the page/component and I would wait for it to be loaded._
