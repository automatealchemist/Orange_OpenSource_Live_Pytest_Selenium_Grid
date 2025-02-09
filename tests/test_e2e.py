import pytest


from pageObjects.Admin import Admin
from utilities.BaseClass import BaseClass
from tests.test_dashboard import DashboardPage
from tests.test_employee_management import EmployeeManagement
from tests.test_admin import AdminManagement
from tests.test_delete_employee import DeleteEmployee


@pytest.mark.usefixtures("setup")
class TestE2E(BaseClass):

    def test_e2e(self, get_employee_data, get_admin_data, get_delete_employee, employee_number):
        log=self.get_logging()
        self.driver.implicitly_wait(10)

        # Initialize page handlers
        dashboard = DashboardPage()
        employee = EmployeeManagement()
        admin = AdminManagement()
        delete = DeleteEmployee()

        # Execute E2E flow with test data
        pi = dashboard.navigate_to_pim(self.driver)
        # Add employee and get the employee number
        emp_number = employee.add_employee(self.driver, pi, get_employee_data, employee_number)

        # Create credentials
        employee.create_credentials(self.driver, pi, get_employee_data)
        employee.update_employee(self.driver, pi, employee_number, get_employee_data)
        log.info("Employee credentials created successfully.")

        # Create admin and store delete page object
        admin_page = Admin(self.driver)  # Create Admin object
        log.info("Admin credentials created successfully.")
        delete_page = admin.create_admin_user(self.driver, get_admin_data)  # Pass only driver and data
        log.info("Admin credentials deleted successfully.")

        # Delete operations
        delete.delete_admin_user(self.driver, delete_page, get_delete_employee)
        delete.delete_employee(self.driver, delete_page, employee_number, get_delete_employee)
        log.info("Employee credentials deleted successfully.")

