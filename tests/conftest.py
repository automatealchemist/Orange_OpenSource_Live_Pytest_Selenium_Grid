import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )



@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_option = Options()
        chrome_option.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)

    #elif browser_name == "firefox":
     #   serv_obj = Service("C:/Users/HELLO/OrangeHRM Demo-Open Source Website Through Pytest/firefoxdriver.exe")
      #  driver = webdriver.Firefox(service=serv_obj)
    elif browser_name == "edge":
       ser_obj = Service(r"C:\Users\HELLO\OrangeHRM Demo-Open Source Website Through Pytest\msedgedriver.exe")
       driver = webdriver.Edge(service=ser_obj)

    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)

    driver.find_element(By.XPATH,
                        '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys(
        "Admin")
    driver.find_element(By.XPATH,
                        '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys(
        "admin123")

    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    request.cls.driver=driver
    yield
    driver.close()
