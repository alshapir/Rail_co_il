import pytest
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from sourse.Set_Browser_2 import Choose
from sourse.navigate_to import Navigate
from sourse.Reports import Reports as rp
from sourse.Login_Function import Log_In_Page
from sourse.Goods_Page_Function import Goods_Page as gp
from sourse.Choose_Goods_Function import Choose_Goods as cg


browser_name="chrome"
driver = WebDriver
main_page_url="https://magento.softwaretestingboard.com/what-is-new.html"
assert_result=""
workbook_row_count = 1
report = rp()
report.create_report()

# class TestBase():
#
#     def __init__(self):
#         self.browser_name="chrome"
#         self.driver=WebDriver
#         self.main_page_url="https://magento.softwaretestingboard.com/what-is-new.html"
#         self.assert_result=""


def test_create_webdriver():
    global driver
    global workbook_row_count
    global report
    driver = Choose().choose_browser(browser_name)
    if isinstance(driver, WebDriver):
        data = {"id":str(workbook_row_count), "Test_Name": "test_create_webdriver","Remarks":"True"}
    else:
        data = {"id":str(workbook_row_count), "Test_Name": "test_create_webdriver", "Remarks": "Fail"}
    report.append_to_report(data)
    workbook_row_count += 1
    assert (assert_result, isinstance(driver, WebDriver))


def test_navigate():
    global driver
    global workbook_row_count
    global report
    driver = Navigate(driver).navigate_to(main_page_url)
    if driver.current_url == main_page_url:
        data={"id":str(workbook_row_count), "Test_Name": "test_navigate", "Remarks": "True"}
    else:
        data = {"id":str(workbook_row_count), "Test_Name": "test_navigate", "Remarks": "False"}
    report.append_to_report(data)
    workbook_row_count += 1
    # Navigate(test_create_webdriver()).navigate_to(main_page_url)
    assert driver.current_url == main_page_url


def test_login_page():
    global driver
    login_page = Log_In_Page(driver)
    login_page.sign_in()
    expected_url = "https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS9wcm90ZXVzLWZpdG5lc3MtamFja3NoaXJ0Lmh0bWw%2C/"
    assert driver.current_url == expected_url

    login_page.insert_email()
    login_page.insert_passwd()
    login_page.sign_in_btn()
    expected_url_2 = "https://magento.softwaretestingboard.com/proteus-fitness-jackshirt.html"
    assert driver.current_url == expected_url_2


def test_choose_goods():
    global driver
    goods_page = gp(driver)
    goods_page.choose_men()
    goods_page.choose_tops()
    goods_page.choose_jackete()
    expected_url_3 = "https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html"
    assert driver.current_url == expected_url_3


def test_goods():
    global driver
    choose = cg(driver)
    choose.main_jacket()
    choose.choose_size()
    choose.choose_color_oranje()
    choose.add_to_cart_btn()
    expected_url_4 = "https://magento.softwaretestingboard.com/proteus-fitness-jackshirt.html"
    assert driver.current_url == expected_url_4


if __name__ == '__main__':
    # run_my_tests = TestBase()
    test_create_webdriver()
    test_navigate()
    test_login_page()
    test_choose_goods()
    test_goods()







