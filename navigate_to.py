import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver


class Navigate:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        if url != "" and url is not None:
            self.driver.get(url)
            self.driver.maximize_window()
            WebDriverWait(self.driver, 10)
            time.sleep(2)
        else:
            print("Not correct URL")
            exit()

        return self.driver


