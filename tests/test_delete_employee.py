import time

import pytest

from tests.conftest import get_employee_data, get_delete_employee
from utilities.BaseClass import BaseClass

@pytest.mark.usefixtures("employee_number")
class DeleteEmployee(BaseClass):
    def delete_admin_user(self, driver,delete, get_delete_employee):
        delete.emp_searches().click()
        time.sleep(2)
        delete.emp_searches().send_keys(get_delete_employee["name"])

        delete.search_button().click()
        time.sleep(5)

        delete.delete_icon().click()
        time.sleep(2)
        delete.delete_confirmation().click()
        time.sleep(5)

    def delete_employee(self, driver, delete, employee_number, get_delete_employee):
        delete.pim_page().click()
        time.sleep(5)

        delete.search_names().click()
        time.sleep(2)
        delete.search_names().send_keys(get_delete_employee["name"])

        # Extract just the number from the tuple
        emp_number = employee_number[0] if isinstance(employee_number, tuple) else employee_number

        delete.number().click()
        delete.number().send_keys(str(emp_number))  # This will now input just the number (e.g., "1248")

        delete.search_emps().click()
        time.sleep(2)
        delete.delete_emps().click()
        time.sleep(2)
        delete.delete_confirm().click()