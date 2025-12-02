import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utility.Excelutility import Excelutility


class TestAdmin:
    def test_return_to_home(self,browser_instance):
        self.driver=browser_instance
        excel_utility = Excelutility()
        valid_username = excel_utility.read_user_data(2, 1)
        valid_password = excel_utility.read_user_data(2, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(valid_username)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(valid_password)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='Sign In']").click()
        self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer'] ").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//a[text()='Home']").click()

        home_url=self.driver.current_url
        assert home_url == "https://groceryapp.uniqassosiates.com/admin/home"

    def test_create_new_user(self,browser_instance):
        self.driver=browser_instance
        excel_utility = Excelutility()
        valid_username = excel_utility.read_user_data(2, 1)
        valid_password = excel_utility.read_user_data(2, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(valid_username)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(valid_password)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='Sign In']").click()
        self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer'] ").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//a[@class='btn btn-rounded btn-danger']").click()
        username=self.driver.find_element(By.XPATH,"//input[@id='username']")
        time.sleep(1)
        username.send_keys("my_name")
        password=self.driver.find_element(By.XPATH,"//input[@id='password']")
        time.sleep(1)
        password.send_keys("my_password")
        userType_dropdown=self.driver.find_element(By.XPATH,"//select[@id='user_type']")
        select=Select(userType_dropdown)
        select.select_by_visible_text("Staff")
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//button[@name='Create']").click()

        #create_user_alert=self.driver.find_element(By.XPATH,"//div[@class='alert alert-danger alert-dismissible']")

        alert = self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")
        alert_text = alert.text.strip()

        expected_messages = [
            "Username already exists.",
            "User Created Successfully"
        ]
        assert any(msg in alert_text for msg in expected_messages), \
            f"Unexpected alert message: {alert_text}"

    def test_search_user(self,browser_instance):
        self.driver=browser_instance
        excel_utility = Excelutility()
        valid_username = excel_utility.read_user_data(2, 1)
        valid_password = excel_utility.read_user_data(2, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(valid_username)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(valid_password)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='Sign In']").click()
        self.driver.find_element(By.XPATH,
                                 "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer'] ").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//a[@class='btn btn-rounded btn-primary']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@id='un']").send_keys("my_user")
        user_type_dropdown=self.driver.find_element(By.XPATH,"//select[@id='ut']")
        select =Select(user_type_dropdown)
        time.sleep(1)
        select.select_by_visible_text("Staff")
        self.driver.find_element(By.XPATH,"//button[@name='Search']").click()



    def test_reset_admin_user_page(self,browser_instance):
        self.driver=browser_instance
        excel_utility = Excelutility()
        valid_username = excel_utility.read_user_data(2, 1)
        valid_password = excel_utility.read_user_data(2, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(valid_username)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(valid_password)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='Sign In']").click()
        self.driver.find_element(By.XPATH,
                                 "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer'] ").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//a[@class='btn btn-rounded btn-warning']").click()

        admin_url=self.driver.current_url
        assert admin_url == "https://groceryapp.uniqassosiates.com/admin/list-admin"

