import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from typing import KeysView
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import random

from pageObjects.Admin import Admin
from pageObjects.Dashboard import Dashboard
from pageObjects.Delete_Employee import Delete_Employee
from pageObjects.Employee_Management import Employee_Management
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")

class TestOne(BaseClass):



   def test_e2e(self):

       # Dashboard
       dashboard=Dashboard(self.driver)
       time.sleep(5)
       dashboard.pim().click()
       time.sleep(3)

       # employee management
       pi = Employee_Management(self.driver)
       pi.add().click()

       time.sleep(5)
       pi.first_name_click().click()

       time.sleep(3)
       pi.first_name_input().send_keys("Angry")

       pi.middle_name_click().click()
       time.sleep(3)
       pi.middle_name_input().send_keys("k")
       time.sleep(2)
       pi.last_name_click().click()
       time.sleep(3)
       pi.last_name_input().send_keys("Bird")

       number = random.randint(1000,9999)
       time.sleep(3)

       element = pi.num()
       element.send_keys(Keys.CONTROL + "a")  # Select all text
       element.send_keys(Keys.BACKSPACE)  # Delete selected text
       element.send_keys(number)

       pi.login_detail().click()

       pi.user_name_click().click()
       pi.user_name_input().send_keys("angrybird")

       pi.password_click().click()
       pi.password_input().send_keys("Password@123")

       time.sleep(2)
       pi.confirm_password_click().click()
       pi.confirm_password_input().send_keys("Password@123")

       pi.save().click()
       time.sleep(10)

       pi.pim_home().click()
       time.sleep(5)

       pi.search_name().click()
       pi.search_name().send_keys("Angry K Bird")

       time.sleep(3)
       pi.search_number().click()
       pi.search_number().send_keys(number)

       pi.search_data().click()

       time.sleep(3)
       pi.edit_button().click()

       time.sleep(3)
       pi.calendar().click()

       time.sleep(3)

       time.sleep(3)
       pi.country_dropdown().click()

       time.sleep(2)
       pi.country_select().click()

       time.sleep(3)

       pi.marital_dropdown().click()
       pi.marital_select().click()

       time.sleep(3)

       pi.date_of_birth().click()

       time.sleep(3)
       pi.gender_options().click()

       time.sleep(3)
       pi.save_buttons().click()

       time.sleep(5)

       pi.blood_group_dropdown().click()

       pi.blood_group_select().click()

       time.sleep(5)
       pi.blood_group_data().click()

       time.sleep(5)

       # Admin Management

       admin_s = Admin(self.driver)
       admin_s.admins().click()
       time.sleep(5)

       #time.sleep(3)
       admin_s.add_emp().click()

       time.sleep(3)
       admin_s.user_role_dropdowns().click()

       time.sleep(2)
       admin_s.user_role_options().click()
       time.sleep(2)
       admin_s.emp_hints().click()
       admin_s.emp_hints().send_keys('Angry K Bird')

       time.sleep(6)

       admin_s.emp_results().click()
       time.sleep(3)
       admin_s.status_dropdowns().click()
       time.sleep(2)
       admin_s.status_options().click()
       time.sleep(3)

       admin_s.emp_names().click()
       admin_s.emp_names().send_keys("Angry K Bird")
       time.sleep(6)

       admin_s.passwords().click()
       admin_s.passwords().send_keys("Password@123")
       time.sleep(2)

       admin_s.confirm_passwords().click()
       admin_s.confirm_passwords().send_keys("Password@123")
       time.sleep(2)

       admin_s.data_save().click()
       time.sleep(10)

       delete = Delete_Employee(self.driver)
       delete.emp_searches().click()
       delete.emp_searches().send_keys("Angry K Bird")

       delete.search_button().click()
       time.sleep(5)

       delete.delete_icon().click()
       time.sleep(5)

       delete.delete_confirmation().click()
       time.sleep(5)

       delete.pim_page().click()
       time.sleep(3)

       delete.search_names().click()
       delete.search_names().send_keys("Angry K Bird")
       time.sleep(5)

       delete.number().click()
       delete.number().send_keys(number)
       time.sleep(3)

       delete.search_emps().click()
       time.sleep(5)

       delete.delete_emps().click()
       time.sleep(5)

       delete.delete_confirm().click()
       time.sleep(5)


       # driver.quit()