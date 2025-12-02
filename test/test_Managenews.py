import time

from selenium.webdriver.common.by import By

from utility.Excelutility import Excelutility


class TestManage_news:
    def test_manage_news(self,browser_instance):
        self.driver=browser_instance
        excel_utility = Excelutility()
        valid_username = excel_utility.read_user_data(2, 1)
        valid_password = excel_utility.read_user_data(2, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(valid_username)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(valid_password)
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[text()='Sign In']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news' and @class='small-box-footer']").click()
        self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/news/add']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//textarea[@id='news']").send_keys("Its snowing!!!")
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//button[@name='create']").click()

        alert_message=self.driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']")
        assert "News Created Successfully" in alert_message.text

    def test_search_news(self,browser_instance):
        self.driver=browser_instance
        excel_utility = Excelutility()
        valid_username = excel_utility.read_user_data(2, 1)
        valid_password = excel_utility.read_user_data(2, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(valid_username)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(valid_password)
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[text()='Sign In']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news' and @class='small-box-footer']").click()
        self.driver.find_element(By.XPATH,"//a[@class='btn btn-rounded btn-primary']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name='un']").send_keys("Its snowing!!!")
        self.driver.find_element(By.XPATH,"//button[@name='Search']").click()
        time.sleep(2)

        row_data=self.driver.find_element(By.XPATH,"//table[@class='table table-bordered table-hover table-sm']/tbody/tr/td")
        assert "Its snowing!!!" not in row_data.text