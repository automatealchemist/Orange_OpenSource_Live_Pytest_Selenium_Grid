import time

class DeleteEmployee:
    def delete_admin_user(self, driver, delete):
        delete.emp_searches().click()
        time.sleep(2)
        delete.emp_searches().send_keys("Angry K Bird")

        delete.search_button().click()
        time.sleep(5)

        delete.delete_icon().click()
        time.sleep(2)
        delete.delete_confirmation().click()

    def delete_employee(self, driver, delete, number):
        delete.pim_page().click()

        delete.search_names().click()
        delete.search_names().send_keys("Angry K Bird")
        delete.number().click()
        delete.number().send_keys(number)

        delete.search_emps().click()
        time.sleep(2)
        delete.delete_emps().click()
        time.sleep(2)
        delete.delete_confirm().click()