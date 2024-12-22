from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, WebDriverException, StaleElementReferenceException
from sourse.Login_elements import Login_Elements as elm_one


class Log_In_Page:

    def __init__(self, driver):
        self.elements = elm_one()
        self.driver = driver

    def sign_in(self):
        try:
            global sign_in_button
            log_in_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(By.XPATH, self.elements.sign_in_button))
            log_in_btn.click()
        except NoSuchElementException:
            self.driver.implicitly_wait(10)
            pass

    def insert_email(self):
        try:
            input_email = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.elements.email_in)))
            input_email.send_keys("alshapir_il@hotmail.com")
        except NoSuchElementException:
            self.driver.implicitly_wait(10)
            pass

    def insert_passwd(self):
        try:
            input_passwd = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.elements.passwd_in)))
            input_passwd.send_keys("As3223as@1")
        except WebDriverException:
            self.driver.implicitly_wait(10)
            pass

    def sign_in_btn(self):
        try:
            signinbtn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, elm_one.sign_in_btn)))
            signinbtn.click()
        except ElementClickInterceptedException:
            self.driver.implicitly_wait(10)
            pass


