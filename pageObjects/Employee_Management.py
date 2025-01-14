from selenium.webdriver.common.by import By

from pageObjects.Admin import Admin
from utilities.BaseClass import BaseClass


class Employee_Management(BaseClass):

    add_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
    firstname = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input')
    middlename = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input')
    lastname = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input')
    username = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input')
    password = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input')
    confirm_password = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input')
    number =(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')
    login_details = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span')
    save_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
    pim_h = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a')
    search = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input')
    search_num = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input')
    search_b = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')
    edit_icon = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[1]')
    cal = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input')
    country = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div')
    country_option = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div[2]/div[83]')
    marital_dropdowns = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div')
    marital_option = (By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]')
    dob = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input')
    gender = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span')
    data_save= (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button')
    #data_save = (By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button')
    blood_group=(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div[1]/div/div[2]/div/div')
    blood_group_option = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[6]')
    blood_group_save = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button')
    admin = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a')

    def __init__(self,driver):
        self.driver=driver

    def add(self):
        return self.driver.find_element(*Employee_Management.add_button)

    def first_name_click(self):
       return  self.driver.find_element(*Employee_Management.firstname)

    def first_name_input(self):
        return self.driver.find_element(*Employee_Management.firstname)

    def middle_name_click(self):
        return self.driver.find_element(*Employee_Management.middlename)

    def middle_name_input(self):
        return self.driver.find_element(*Employee_Management.middlename)

    def last_name_click(self):
        return self.driver.find_element(*Employee_Management.lastname)

    def last_name_input(self):
        return self.driver.find_element(*Employee_Management.lastname)

    def user_name_click(self):
        return self.driver.find_element(*Employee_Management.username)

    def user_name_input(self):
        return self.driver.find_element(*Employee_Management.username)

    def password_click(self):
        return self.driver.find_element(*Employee_Management.password)

    def password_input(self):
        return self.driver.find_element(*Employee_Management.password)

    def confirm_password_click(self):
        return self.driver.find_element(*Employee_Management.confirm_password)

    def confirm_password_input(self):
        return self.driver.find_element(*Employee_Management.confirm_password)

    def num(self):
        return self.driver.find_element(*Employee_Management.number)

    def login_detail(self):
        return self.driver.find_element(*Employee_Management.login_details)

    def save(self):
        return self.driver.find_element(*Employee_Management.save_button)

    def pim_home(self):
        return self.driver.find_element(*Employee_Management.pim_h)

    def search_name(self):
        return self.driver.find_element(*Employee_Management.search)

    def search_number(self):
        return self.driver.find_element(*Employee_Management.search_num)

    def search_data(self):
        return self.driver.find_element(*Employee_Management.search_b)

    def edit_button(self):
        return self.driver.find_element(*Employee_Management.edit_icon)

    def calendar(self):
        return self.driver.find_element(*Employee_Management.cal)

    def country_dropdown(self):
        return self.driver.find_element(*Employee_Management.country)

    def country_select(self):
        return self.driver.find_element(*Employee_Management.country_option)

    def marital_dropdown(self):
        return self.driver.find_element(*Employee_Management.marital_dropdowns)

    def marital_select(self):
        return self.driver.find_element(*Employee_Management.marital_option)

    def date_of_birth(self):
        return self.driver.find_element(*Employee_Management.dob)

    def gender_options(self):
        return self.driver.find_element(*Employee_Management.gender)

    def save_buttons(self):
        return self.driver.find_element(*Employee_Management.data_save)

    def blood_group_dropdown(self):
        return self.driver.find_element(*Employee_Management.blood_group)

    def blood_group_select(self):
        return self.driver.find_element(*Employee_Management.blood_group_option)

    def blood_group_data(self):
        return self.driver.find_element(*Employee_Management.blood_group_save)

    def admins(self):
        self.driver.find_element(*Employee_Management.admin).click()
        admin_s = Admin(self.driver)
        return admin_s

