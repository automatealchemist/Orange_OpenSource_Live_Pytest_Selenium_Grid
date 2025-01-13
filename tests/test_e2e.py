import pytest
from utilities.BaseClass import BaseClass
from tests.test_dashboard import DashboardPage
from tests.test_employee_management import EmployeeManagement
from tests.test_admin import AdminManagement
from tests.test_delete_employee import DeleteEmployee

@pytest.mark.usefixtures("setup")
class TestE2E(BaseClass):
    def test_e2e(self):

        # Set implicit wait
        self.driver.implicitly_wait(10)

        # Initialize page classes
        dashboard = DashboardPage()
        employee = EmployeeManagement()
        admin = AdminManagement()
        delete = DeleteEmployee()

        # Execute E2E flow
        pi = dashboard.navigate_to_pim(self.driver)

        emp_number = employee.add_employee(self.driver, pi)
        employee.create_credentials(self.driver, pi)

        admin_s = employee.update_employee(self.driver, pi, emp_number)

        delete_page = admin.create_admin_user(self.driver, admin_s)

        delete.delete_admin_user(self.driver, delete_page)
        delete.delete_employee(self.driver, delete_page, emp_number)

