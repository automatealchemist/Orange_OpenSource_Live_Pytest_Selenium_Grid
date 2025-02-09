import random
import inspect
import logging
import pytest
import os

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

    def get_logging(self):
        # the below line will give the name from which this method is called
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        log_dir = "C:/Users/HELLO/OrangeHRMDemoOpenSourceWebsiteThroughPytest/utilities"
        log_file = os.path.join(log_dir, "logfile.log")

        # Ensure the directory exists
        os.makedirs(log_dir, exist_ok=True)

        # Setup logging
        filehandler = logging.FileHandler(log_file)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        # we can also set level from where we want to print logs

        logger.setLevel(logging.DEBUG)  # it will print from INFO level
        return logger


