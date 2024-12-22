from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, WebDriverException, StaleElementReferenceException
from sourse.choose_goods_elements import Choose_Goods_Elements as elem_three


class Choose_Goods:

    def __init__(self, driver):
        self.elements = elem_three()
        self.driver = driver


    def main_jacket(self):
        try:
            main_jacket_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.elements.main_jacket)))
            main_jacket_btn.click()
        except NoSuchElementException:
            self.driver.implicitly_wait(10)
            pass

    def choose_size(self):
        try:
            size_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.elements.size)))
            size_btn.click()
        except NoSuchElementException:
            self.driver.implicitly_wait(10)
            pass

    def choose_color_oranje(self):
        try:
            color_oranje_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.elements.color_oranje)))
            color_oranje_btn.click()
        except NoSuchElementException:
            self.driver.implicitly_wait(10)
            pass

    def add_to_cart_btn(self):
        try:
            add_to_cart_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.elements.add_to_cart_btn)))
            add_to_cart_btn.click()
        except NoSuchElementException:
            self.driver.implicitly_wait(10)
            pass