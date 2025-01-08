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

from pageObjects.Dashboard import Dashboard
from pageObjects.Employee_Management import Employee_Management
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")

class TestOne(BaseClass):



   def test_e2e(self):

       '''
       driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
       time.sleep(5)

       driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys(
           "Admin")
       driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys(
           "admin123")

       driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
       time.sleep(5)
       '''
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

       element = self.driver.find_element(By.XPATH,
                                          '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')
       element.send_keys(Keys.CONTROL + "a")  # Select all text
       element.send_keys(Keys.BACKSPACE)  # Delete selected text
       element.send_keys(number)

       self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span').click()

       pi.user_name_click().click()
       pi.user_name_input().send_keys("angrybird")

       pi.password_click().click()
       pi.password_input().send_keys("Password@123")

       time.sleep(2)
       pi.confirm_password_click().click()
       pi.confirm_password_input().send_keys("Password@123")


       self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()

       time.sleep(10)


       self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a').click()
       time.sleep(5)


       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').click()
       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys(
           "Angry k Bird")
       time.sleep(3)
       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div').click()
       time.sleep(5)

       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input').click()
       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input').send_keys(
           number)
       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
       time.sleep(3)
       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[1]').click()
       time.sleep(3)
       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input').click()
       time.sleep(3)
       # driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input').clear()
       # driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input').send_keys("2024-12-12")
       time.sleep(3)
       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div').click()
       time.sleep(2)
       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div[2]/div[83]').click()
       time.sleep(3)
       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div').click()
       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]').click()
       time.sleep(3)

       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input').click()
       # driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input').clear()
       # driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input').send_keys('1995-21-09')
       time.sleep(3)
       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span').click()
       time.sleep(3)

       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button').click()
       time.sleep(5)
       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div[1]/div/div[2]/div/div').click()

       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[6]').click()
       time.sleep(5)
       self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button').click()
       time.sleep(5)

       # self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()

       time.sleep(10)
       '''
       self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()
       time.sleep(3)
       self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
       time.sleep(3)
       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div').click()
       time.sleep(2)
       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]/span').click()
       time.sleep(2)

       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input').click()
       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input').send_keys(
           'Angry K Bird')
       time.sleep(6)
       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div').click()
       time.sleep(3)
       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div').click()
       time.sleep(2)
       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[2]').click()
       time.sleep(3)
       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input').click()
       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input').send_keys(
           "Angry K Bird")
       time.sleep(6)

       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input').click()
       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input').click()
       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input').send_keys(
           "Password@123")
       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input').click()
       self.driver.find_element(By.XPATH,
                           '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input').send_keys(
           'Password@123')
       time.sleep(2)
       self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]').click()
       time.sleep(10)

       self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input').click()
       self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input').send_keys("Angry K Bird")
       self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
       time.sleep(5)

       self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[6]/div/button[1]/i').click()
       time.sleep(5)
       self.driver.find_element(By.XPATH,
                                '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]').click()
       time.sleep(5)
       self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
       time.sleep(5)
       self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').click()
       time.sleep(2)
       self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys("Angry k Bird")
       time.sleep(3)
       self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div').click()
       time.sleep(5)

       self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input').click()
       time.sleep(2)
       self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input').send_keys(number)
       time.sleep(3)
       self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
       time.sleep(5)
       self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]').click()
       time.sleep(3)
       self.driver.find_element(By.XPATH,'//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]').click()
       time.sleep(5)
'''
       # driver.quit()