from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, WebDriverException, StaleElementReferenceException
from sourse.goods_page_elements import Goods_Page_Elements as elem_two



class Goods_Page:
    def __init__(self, driver):
        self.elements = elem_two()
        self.driver=driver

    def choose_men(self):
        try:
            men_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(By.XPATH, self.elements.men_btn))
            men_btn.click()
        except NoSuchElementException:
            self.driver.implicitly_wait(10)
            pass

    def choose_tops(self):
        try:
            tops_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(By.XPATH, self.elements.tops))
            tops_btn.click()
        except NoSuchElementException:
            self.driver.implicitly_wait(10)
            pass

    def choose_jackete(self):
        try:
            jackets_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(By.XPATH, self.elements.jackets))
            jackets_btn.click()
        except NoSuchElementException:
            self.driver.implicitly_wait(10)
            pass