
from selenium.webdriver.common.by import By


class Delete_Employee:
    emp_search = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input')
    search_b = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')
    delete = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[6]/div/button[1]/i')
    delete_c = (By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]')
    pim_p = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
    search_name = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input')
    num = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input')
    search_pim = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')
    delete_pim = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]')
    delete_con = (By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]')

    def __init__(self,driver):
        self.driver = driver

    def emp_searches(self):
        return self.driver.find_element(*Delete_Employee.emp_search)

    def search_button(self):
        return self.driver.find_element(*Delete_Employee.search_b)

    def delete_icon(self):
        return self.driver.find_element(*Delete_Employee.delete)

    def delete_confirmation(self):
        return self.driver.find_element(*Delete_Employee.delete_c)

    def pim_page(self):
        return self.driver.find_element(*Delete_Employee.pim_p)

    def search_names(self):
        return self.driver.find_element(*Delete_Employee.search_name)

    def number(self):
        return self.driver.find_element(*Delete_Employee.num)

    def search_emps(self):
        return self.driver.find_element(*Delete_Employee.search_pim)

    def delete_emps(self):
        return self.driver.find_element(*Delete_Employee.delete_pim)

    def delete_confirm(self):
        return self.driver.find_element(*Delete_Employee.delete_con)
