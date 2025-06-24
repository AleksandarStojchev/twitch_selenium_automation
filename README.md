# twitch_selenium_automation

**Project Structure**

**BasePage:** Defines common browser interaction methods.

**HomePage:** Contains locators and actions specific to the Twitch home page.

**BaseTest:** Sets up and tears down the browser session for each test.

**TestsSearch:** Implements the test case for searching and interacting with streamers.


**Test running GIF**

![twitch_test_running](https://github.com/user-attachments/assets/5616cb8a-a274-447c-9e0b-f955706630d9)

--------------------------------------
*Pre-requisite:*

The test must be run using the Mobile emulator from Google Chrome
Selenium (python) must be used for this test case.

*Steps*

1 go to Twitch

2 click in the search icon

3 input StarCraft II

4 scroll down 2 times

5 Select one streamer

6 on the streamer page wait until all is load and take a screenshot


NOTES:
Some streamers will have a modal or pop-up before loading the video, the Auto test case should be able to handle this pop-up.
(optional) use pytest as a test runner
