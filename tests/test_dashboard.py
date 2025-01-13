

from pageObjects.Dashboard import Dashboard
from utilities.BaseClass import BaseClass

class DashboardPage:
    def navigate_to_pim(self, driver):
        dashboard = Dashboard(driver)
        return dashboard.pim()
