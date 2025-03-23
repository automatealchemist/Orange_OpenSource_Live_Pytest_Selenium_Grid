import random
from utilities.BaseClass import BaseClass

class EmployeeManagementData:
    name_data = BaseClass.generate_full_name()

    test_employee_data = [
        {
            "firstname": name_data["first_name"],
            "middlename": name_data["middle_name"],
            "lastname": name_data["last_name"],
            "username": name_data["user_name"],
            "password": "Password@123",
            "confirmpassword": "Password@123",

        }
    ]