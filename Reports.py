from datetime import datetime
import os
import csv


class Reports:

    def __init__(self):
        self.headerList = ['id', 'Test_Name', 'Statuss', 'Remarks']
        now = datetime.now()  # current date and time
        date_time=now.strftime("%m_%d_%Y_%H_%M_%S")
        current_path = os.getcwd()
        self.report_name = current_path + "\\Report_" + date_time + ".csv"

    def create_report(self):
        with open(self.report_name, 'w') as file:
            dw=csv.DictWriter(file, delimiter=',', fieldnames=self.headerList)
            dw.writeheader()
            file.close()

    def append_to_report(self, data):
        with open(self.report_name, 'a', newline='') as csvfile:
            dwr = csv.DictWriter(csvfile, fieldnames=self.headerList)
            dwr.writerow(data)
            csvfile.close()





# with open(report_name, 'a', newline='') as csvfile:
#     headerList=['id', 'Test_Name', 'Status', 'Remarks']
#     writer=csv.DictWriter(csvfile, fieldnames=headerList)
#     writer.writerow({'id': '1', 'Test_Name': 'login', 'Status': 'Pass', 'Remarks': 'New Test'})

# def set_workbook_field(column, row_number):
#     col_name = column + row_number
#     return col_name
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.wait import WebDriverWait
# from datetime import datetime
# import os
# import csv
# from tkinter import filedialog
# import xlsxwriter
# import pandas as pd
# import inspect
# import json
# from typing import Callable
# from selenium import webdriver