import random

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

from TestData.AdminData import AdminData
from TestData.DeleteEmployeeData import DeleteEmployeeData
from TestData.EmployeeManagementData import EmployeeManagementData

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_option = Options()
        chrome_option.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
    elif browser_name == "edge":
        path = r"C:\Users\HELLO\OrangeHRM Demo-Open Source Website Through Pytest\msedgedriver.exe"
        ser_obj = Service(path)
        driver = webdriver.Edge(service=ser_obj)

    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)

    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.fixture(params=EmployeeManagementData.test_employee_data)
def get_employee_data(request):
    return request.param

@pytest.fixture(params=AdminData.test_admin_data)
def get_admin_data(request):
    return request.param

@pytest.fixture(params=DeleteEmployeeData.test_delete_employee_data)
def get_delete_employee(request):
    return request.param

@pytest.fixture(scope="class")
def employee_number():
    return random.randint(1000, 9999)


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")