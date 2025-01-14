import random

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
class BaseClass:
    def set_implicit_wait(self, driver, time_in_seconds):
        """Set the implicit wait for the driver."""
        driver.implicitly_wait(time_in_seconds)

    emp_number = None  # Class variable to store the number

    def random_number(self):
        if BaseClass.emp_number is None:  # Generate only if not already generated
            BaseClass.emp_number = random.randint(1000, 9999)
        return BaseClass.emp_number


