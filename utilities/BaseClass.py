import random
import inspect
import logging
import pytest
import os
import random
import string

@pytest.mark.usefixtures("setup")
class BaseClass:
    _generated_name = None
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

     # Store the generated name once

    @classmethod
    def generate_full_name(cls):

        if cls._generated_name is None:  # Generate only if not already stored
            first_name = ''.join(random.choices(string.ascii_letters, k=5))
            middle_name = ''.join(random.choices(string.ascii_letters, k=5))
            last_name = ''.join(random.choices(string.ascii_letters, k=5))
            full_name = f"{first_name} {middle_name} {last_name}"
            user_name = f"{first_name.lower()}.{last_name.lower()}"

            # Store generated names (to be reused everywhere)
            cls._generated_name = {
                "first_name": first_name,
                "middle_name": middle_name,
                "last_name": last_name,
                "full_name": full_name,
                "user_name": user_name
            }

        return cls._generated_name