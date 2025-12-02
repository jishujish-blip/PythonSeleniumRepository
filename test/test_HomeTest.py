import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utility.Excelutility import Excelutility


class Test_HomeTest:
    def test_logout(self,browser_instance):
        self.driver=browser_instance
        excel_utility=Excelutility()
        valid_username=excel_utility.read_user_data(2,1)
        valid_password=excel_utility.read_user_data(2,2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        self.driver.find_element(By.XPATH,"//input[@name='username']").send_keys(valid_username)
        self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys(valid_password)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[text()='Sign In']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//li[@class='nav-item dropdown']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//a/i[@class='ace-icon fa fa-power-off']").click()
        time.sleep(2)

