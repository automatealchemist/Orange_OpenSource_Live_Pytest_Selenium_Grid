from selenium.webdriver.common.by import By


class Dashboard:

    def __init__(self,driver):
        self.driver = driver


    p = (By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')

    def pim(self):
        return self.driver.find_element(*Dashboard.p)
        #self. driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')