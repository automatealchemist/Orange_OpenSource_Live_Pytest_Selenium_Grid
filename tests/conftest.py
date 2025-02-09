import random
import os
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from TestData.AdminData import AdminData
from TestData.DeleteEmployeeData import DeleteEmployeeData
from TestData.EmployeeManagementData import EmployeeManagementData
driver = None
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(scope="class")
def setup(request):
    global driver
    # Setup WebDriver based on the browser_name passed
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_option = Options()
        chrome_option.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
    elif browser_name == "edge":
        #path = r"/\msedgedriver.exe"
        #ser_obj = Service(path)
        #driver = webdriver.Edge(service=ser_obj)
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        print("Unsupported or invalid browser name.")
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)

    # Perform login actions
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)  # Correct hook wrapper
def pytest_runtest_makereport(item):
    global driver
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":  # Screenshot on call or setup failure
        if report.failed:  # This will be True for ANY failure, including AttributeError
            root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
            reports_dir = os.path.join(root_dir, "reports")
            screenshots_dir = os.path.join(reports_dir, "screenshots")

            os.makedirs(screenshots_dir, exist_ok=True)  # Ensure directory exists

            file_name = report.nodeid.replace("::", "_").replace("/", "_") + ".png" #Replace / with _ for windows path compatibility
            file_path = os.path.join(screenshots_dir, file_name)
            relative_path = os.path.join("screenshots", file_name)

            driver = getattr(item.cls, "driver", None)
            if driver:
                try:  # Try to capture, handle exceptions
                    print(f"Capturing screenshot at: {file_path}")
                    driver.get_screenshot_as_file(file_path)
                    print(f"Screenshot saved to: {file_path}")

                    html = f'<div><img src="{relative_path}" alt="screenshot" style="width:100%;height:auto;" /></div>'
                    extra.append(pytest_html.extras.html(html))
                except Exception as e:  # Handle potential screenshot errors
                    print(f"Error capturing screenshot: {e}")
            else:
                print("Driver not available to capture screenshot.")

        report.extras = extra  # Correct attribute name

def pytest_configure(config):
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    reports_dir = os.path.join(root_dir, "reports")
    screenshots_dir = os.path.join(reports_dir, "screenshots")

    os.makedirs(screenshots_dir, exist_ok=True)
    print(f"Ensured directory exists: {screenshots_dir}")



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