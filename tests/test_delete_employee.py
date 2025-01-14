import time

import pytest

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

    def delete_employee(self,driver, delete, number,get_delete_employee,employee_number):

        delete.pim_page().click()
        time.sleep(3)

        delete.search_names().click()
        delete.search_names().send_keys(get_delete_employee["name"])
        delete.number().click()
        delete.number().send_keys(str(employee_number))

        delete.search_emps().click()
        time.sleep(2)
        delete.delete_emps().click()
        time.sleep(2)
        delete.delete_confirm().click()