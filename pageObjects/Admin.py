from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.dom import discard_search_results

from pageObjects.Delete_Employee import Delete_Employee


class Admin:

    add = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
    user_role_dropdown = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div')
    user_role_option = (By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]/span')
    emp_hint = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input')
    emp_result =(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div')
    status_dropdown = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div')
    status_option =(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[2]')
    emp_name = (By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input')
    password = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input')
    confirm_password = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input')
    data_saves = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]')

    admin = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a')


    def __init__(self,driver):
        self.driver= driver





    def add_emp(self):
        return self.driver.find_element(*Admin.add)

    def user_role_dropdowns(self):
        return self.driver.find_element(*Admin.user_role_dropdown)

    def user_role_options(self):
        return self.driver.find_element(*Admin.user_role_option)

    def emp_hints(self):
        return self.driver.find_element(*Admin.emp_hint)

    def emp_results(self):
        return self.driver.find_element(*Admin.emp_result)

    def status_dropdowns(self):
        return self.driver.find_element(*Admin.status_dropdown)

    def status_options(self):
        return self.driver.find_element(*Admin.status_option)

    def emp_names(self):
        return self.driver.find_element(*Admin.emp_name)

    def passwords(self):
        return self.driver.find_element(*Admin.password)

    def confirm_passwords(self):
        return self.driver.find_element(*Admin.confirm_password)

    def data_save(self):
        return self.driver.find_element(*Admin.data_saves)

    def delete_b(self):
        self.driver.find_element(*Admin.admin).click()
        delete = Delete_Employee(self.driver)
        return delete












