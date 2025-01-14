import pytest
from selenium.webdriver import Keys
import time
import random

from TestData import EmployeeManagementData
from selenium.webdriver import Keys
import time
import random

from utilities.BaseClass import BaseClass

@pytest.mark.usefixtures("employee_number")
class EmployeeManagement(BaseClass):
    def add_employee(self, driver, pi, get_employee_data, employee_number):
        pi.add().click()
        time.sleep(5)

        # First Name
        pi.first_name_click().click()
        pi.first_name_input().send_keys(get_employee_data["firstname"])

        # Middle Name
        pi.middle_name_click().click()
        pi.middle_name_input().send_keys(get_employee_data["middlename"])

        # Last Name
        pi.last_name_click().click()
        pi.last_name_input().send_keys(get_employee_data["lastname"])

        # Generate random employee number

        element = pi.num()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(str(employee_number))

        return str(employee_number), get_employee_data

    def create_credentials(self, driver, pi, get_employee_data):
        pi.login_detail().click()

        # Username
        pi.user_name_click().click()
        pi.user_name_input().send_keys(get_employee_data["username"])

        # Password
        pi.password_click().click()
        pi.password_input().send_keys(get_employee_data["password"])

        # Confirm Password
        pi.confirm_password_click().click()
        pi.confirm_password_input().send_keys(get_employee_data["confirmpassword"])

        pi.save().click()
        time.sleep(10)


    def update_employee(self, driver, pi, employee_number, get_employee_data):  # Fixed parameter order
        pi.pim_home().click()
        time.sleep(5)

        # Search using full name from test data
        full_name = f"{get_employee_data['firstname']} {get_employee_data['middlename']} {get_employee_data['lastname']}"

        pi.search_name().click()
        pi.search_name().send_keys(full_name)
        time.sleep(3)

        pi.search_number().click()
        pi.search_number().send_keys(str(employee_number))
        time.sleep(3)
        pi.search_data().click()
        time.sleep(5)

        pi.edit_button().click()
        time.sleep(3)

        pi.calendar().click()
        pi.country_dropdown().click()
        pi.country_select().click()
        pi.marital_dropdown().click()
        pi.marital_select().click()
        pi.date_of_birth().click()
        pi.gender_options().click()
        pi.save_buttons().click()
        time.sleep(5)

        pi.blood_group_dropdown().click()
        pi.blood_group_select().click()
        pi.blood_group_data().click()
        time.sleep(5)

        return pi.admins()
'''
class EmployeeManagement:
    def __init__(self):
        self.test_data = EmployeeManagementData.get_test_employee_data()

    def add_employee(self, driver, pi, get_employee_data):
        pi.add().click()
        time.sleep(5)

        # First Name
        pi.first_name_click().click()
        pi.first_name_input().send_keys(get_employee_data["firstname"])

        # Middle Name
        pi.middle_name_click().click()
        pi.middle_name_input().send_keys(get_employee_data["middlename"])

        # Last Name
        pi.last_name_click().click()
        pi.last_name_input().send_keys(get_employee_data["lastname"])

        # Generate random employee number
        number = random.randint(1000, 9999)
        element = pi.num()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(number)

        return number, get_employee_data

    def create_credentials(self, driver, pi, get_employee_data):
        pi.login_detail().click()

        # Username
        pi.user_name_click().click()
        pi.user_name_input().send_keys(get_employee_data["username"])

        # Password
        pi.password_click().click()
        pi.password_input().send_keys(get_employee_data["password"])

        # Confirm Password
        pi.confirm_password_click().click()
        pi.confirm_password_input().send_keys(get_employee_data["confirmpassword"])

        pi.save().click()
        time.sleep(5)

    def update_employee(self, driver, pi, number, get_employee_data):
        pi.pim_home().click()
        time.sleep(5)

        # Search using full name from test data
        full_name = f"{get_employee_data['firstname']} {get_employee_data['middlename']} {get_employee_data['lastname']}"
        pi.search_name().click()
        pi.search_name().send_keys(full_name)

        pi.search_number().click()
        pi.search_number().send_keys(number)
        pi.search_data().click()
        time.sleep(3)

        pi.edit_button().click()
        time.sleep(3)

        pi.calendar().click()
        pi.country_dropdown().click()
        pi.country_select().click()
        pi.marital_dropdown().click()
        pi.marital_select().click()
        pi.date_of_birth().click()
        pi.gender_options().click()
        pi.save_buttons().click()
        time.sleep(5)

        pi.blood_group_dropdown().click()
        pi.blood_group_select().click()
        pi.blood_group_data().click()
        time.sleep(5)

        return pi.admins()
'''
    #@pytest.fixture(params=["Angry", "k", "bird"])
    #def getdata(self,request):
        #return request.param

    # @pytest.fixture(params=[{"firstname""Angry","middlename" : "k","lastname" : "bird"])
    # def getdata(self,request):
    # return request.param

    # @pytest.fixture(params=EmployeeManagementData.test_employee_management_data)
    # def getdata(self,request):
    # return request.param



