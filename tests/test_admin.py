import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pageObjects.Delete_Employee import Delete_Employee


class AdminManagement:
    def create_admin_user(self, driver, get_admin_data):
        # Wait for the page to load and the add button to be clickable
        wait = WebDriverWait(driver, 10)
        add_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
        ))
        add_button.click()

        # Wait for and interact with user role dropdown
        user_role = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div')
        ))
        user_role.click()

        # Select user role option
        user_role_option = wait.until(EC.element_to_be_clickable(
            (By.XPATH,
             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]/span')
        ))
        user_role_option.click()

        # Employee name hint field
        emp_hint = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input')
        ))
        emp_hint.click()
        emp_hint.send_keys(get_admin_data["name"])
        time.sleep(3)

        # Wait for and select employee result
        emp_result = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div')
        ))
        emp_result.click()
        time.sleep(2)

        # Status dropdown
        status = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div')
        ))
        status.click()

        # Select status option
        status_option = wait.until(EC.element_to_be_clickable(
            (
            By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[2]')
        ))
        status_option.click()

        # Username field
        username = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input')
        ))
        username.click()
        username.send_keys(get_admin_data["name"])

        # Password fields
        password = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input')
        ))
        password.click()
        password.send_keys(get_admin_data["password"])

        confirm_password = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input')
        ))
        confirm_password.click()
        confirm_password.send_keys(get_admin_data["confirmpassword"])

        # Save button
        save_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]')
        ))
        save_button.click()

        # Wait for save operation to complete
        time.sleep(5)
        delete = Delete_Employee(driver)
        return delete

        #return admin_s.delete_b()