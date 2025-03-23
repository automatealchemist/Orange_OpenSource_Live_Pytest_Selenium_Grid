import random


from TestData.AdminData import AdminData
from TestData.DeleteEmployeeData import DeleteEmployeeData
from TestData.EmployeeManagementData import EmployeeManagementData

import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

GRID_URL = "http://localhost:4444/wd/hub"

# Define the browsers list dynamically
BROWSERS = ["chrome", "edge","firefox"]


@pytest.fixture(params=BROWSERS, scope="class")
def setup(request):
# Fixture to initialize WebDriver for selected browsers in parallel.

    browser_name = request.param
    options = None

    if browser_name == "chrome":
        options = ChromeOptions()
    elif browser_name == "edge":
        options = EdgeOptions()
    elif browser_name == "firefox":
        options = FirefoxOptions()
    else:
        pytest.fail("Unsupported or invalid browser name.")

    # Connect to Selenium Grid
    driver = webdriver.Remote(
        command_executor=GRID_URL,
        options=options
    )

    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)

    # Perform login actions
    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """Hook to capture screenshots on test failure."""
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        if report.failed:
            root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
            reports_dir = os.path.join(root_dir, "reports")
            screenshots_dir = os.path.join(reports_dir, "screenshots")

            os.makedirs(screenshots_dir, exist_ok=True)

            file_name = report.nodeid.replace("::", "_").replace("/", "_") + ".png"
            file_path = os.path.join(screenshots_dir, file_name)
            relative_path = os.path.join("screenshots", file_name)

            driver = getattr(item.cls, "driver", None)
            if driver:
                try:
                    print(f"Capturing screenshot at: {file_path}")
                    driver.get_screenshot_as_file(file_path)
                    print(f"Screenshot saved to: {file_path}")

                    html = f'<div><img src="{relative_path}" alt="screenshot" style="width:100%;height:auto;" /></div>'
                    extra.append(pytest_html.extras.html(html))
                except Exception as e:
                    print(f"Error capturing screenshot: {e}")
            else:
                print("Driver not available to capture screenshot.")

        report.extras = extra


def pytest_configure(config):
    """Ensures reports directory exists."""
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
