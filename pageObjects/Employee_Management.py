from selenium.webdriver.common.by import By


class Employee_Management:

    add_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
    firstname = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input')
    middlename = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input')
    lastname = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input')
    username = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input')
    password = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input')
    confirm_password = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input')

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



    '''
    time.sleep(5)

    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input').click()
    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input').send_keys(
        "k")
    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input').click()
    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input').send_keys(
        "Bird")

    number = random.randint(1000, 9999)
    time.sleep(3)

    element = self.driver.find_element(By.XPATH,
                                       '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')
    element.send_keys(Keys.CONTROL + "a")  # Select all text
    element.send_keys(Keys.BACKSPACE)  # Delete selected text
    element.send_keys(number)

    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span').click()
    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input').click()
    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input').send_keys(
        'angrybird')
    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input').click()
    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input').send_keys(
        'Password@123')
    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input').click()
    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input').send_keys(
        'Password@123')

    self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()

    time.sleep(10)

    self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a').click()
    time.sleep(5)

    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').click()
    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys(
        "Angry k Bird")
    time.sleep(3)
    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div').click()
    time.sleep(5)

    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input').click()
    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input').send_keys(
        number)
    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
    time.sleep(3)
    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[1]').click()
    time.sleep(3)
    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input').click()
    time.sleep(3)
    # driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input').clear()
    # driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input').send_keys("2024-12-12")
    time.sleep(3)
    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div').click()
    time.sleep(2)
    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div[2]/div[83]').click()
    time.sleep(3)
    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div').click()
    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]').click()
    time.sleep(3)

    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input').click()
    # driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input').clear()
    # driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input').send_keys('1995-21-09')
    time.sleep(3)
    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span').click()
    time.sleep(3)

    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button').click()
    time.sleep(5)
    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div[1]/div/div[2]/div/div').click()

    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[6]').click()
    time.sleep(5)
    self.driver.find_element(By.XPATH,
                             '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button').click()
    time.sleep(5)
'''