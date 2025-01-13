import time


class AdminManagement:
    def create_admin_user(self, driver, admin_s):
        admin_s.add_emp().click()

        admin_s.user_role_dropdowns().click()
        admin_s.user_role_options().click()

        admin_s.emp_hints().click()
        admin_s.emp_hints().send_keys('Angry K Bird')
        time.sleep(3)
        admin_s.emp_results().click()

        admin_s.status_dropdowns().click()
        admin_s.status_options().click()

        admin_s.emp_names().click()
        admin_s.emp_names().send_keys("Angry K Bird")
        admin_s.passwords().click()
        admin_s.passwords().send_keys("Password@123")
        admin_s.confirm_passwords().click()
        admin_s.confirm_passwords().send_keys("Password@123")

        admin_s.data_save().click()
        time.sleep(5)

        return admin_s.delete_b()