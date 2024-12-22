from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import codecs
import os


class Choose:

    def __init__(self):
        self.driver = WebDriver
        self.actions = ActionChains
        self.wait = WebDriverWait

    def choose_browser(self, browser_name):
        if browser_name == "" or browser_name is None:
            browser_name = "chrome"

        if str(browser_name).lower() == "chrome":
            try:
                self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            except Exception:
                print("Driver not created")
                exit()
            self.wait = WebDriverWait(self.driver, 10)
            self.actions = ActionChains(self.driver)

        if str(browser_name).lower() == "firefox":
            pass

        return self.driver

    def teardown_method(self):
        self.driver.quit()
# Choose().choose_browser("")