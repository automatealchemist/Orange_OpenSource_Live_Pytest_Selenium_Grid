from selenium.webdriver import Keys
import time
import random


class EmployeeManagement:
    def add_employee(self, driver, pi):
        pi.add().click()
        time.sleep(5)

        pi.first_name_click().click()
        pi.first_name_input().send_keys("Angry")

        pi.middle_name_click().click()
        pi.middle_name_input().send_keys("k")

        pi.last_name_click().click()
        pi.last_name_input().send_keys("Bird")

        number = random.randint(1000, 9999)
        element = pi.num()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(number)

        return number

    def create_credentials(self, driver, pi):
        pi.login_detail().click()
        pi.user_name_click().click()
        pi.user_name_input().send_keys("angrybird")

        pi.password_click().click()
        pi.password_input().send_keys("Password@123")

        pi.confirm_password_click().click()
        pi.confirm_password_input().send_keys("Password@123")

        pi.save().click()
        time.sleep(5)

    def update_employee(self, driver, pi, number):
        pi.pim_home().click()
        time.sleep(5)

        pi.search_name().click()
        pi.search_name().send_keys("Angry K Bird")
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