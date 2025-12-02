import openpyxl
import pytest
from selenium.webdriver.common.by import By

from Python_selenium_package.pages.Loginpage import Loginpage
from utility.Excelutility import Excelutility


class Test_login:
    @pytest.mark.run(order=1)
    def test_login_with_valid_credentials(self, browser_instance):
        self.driver = browser_instance  # webdriver instance is holding browser_instance
        # driver is local variable in browser_instance function
        excelutility = Excelutility()
        valid_username_value = excelutility.read_user_data(2, 1)  # username value form excel sheet
        valid_password_value = excelutility.read_user_data(2, 2)  # password value form excel sheet
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")

        loginpage=Loginpage(self.driver)
        loginpage.enter_username(valid_username_value)
        loginpage.enter_password(valid_password_value)
        loginpage.sign_in(self.driver)

        # username_textbox = self.driver.find_element(By.XPATH, "//input[@name='username']")
        # username_textbox.send_keys(valid_username_value)
        # password_textbox = self.driver.find_element(By.XPATH, "//input[@name='password']")
        # password_textbox.send_keys(valid_password_value)
        # self.driver.find_element(By.XPATH, "//button[text()='Sign In']").click()

        url_name=self.driver.current_url
        assert url_name == "https://groceryapp.uniqassosiates.com/admin"

    @pytest.mark.run(order=2)
    def test_login_with_invalid_username(self, browser_instance):
        self.driver = browser_instance
        excelutility=Excelutility()
        invalid_username=excelutility.read_user_data(4,1)
        valid_password = excelutility.read_user_data(4,2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        username_textbox = self.driver.find_element(By.XPATH, "//input[@name='username']")
        username_textbox.send_keys(invalid_username)
        password_textbox = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password_textbox.send_keys(valid_password)
        self.driver.find_element(By.XPATH, "//button[text()='Sign In']").click()

        url_name= self.driver.current_url
        assert url_name == "https://groceryapp.uniqassosiates.com/admin/login"

    @pytest.mark.run(order=3)
    def test_login_with_invalid_password(self, browser_instance):
        self.driver = browser_instance
        excelutility = Excelutility()
        valid_username = excelutility.read_user_data(3, 1)
        invalid_password = excelutility.read_user_data(3, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        username_textbox = self.driver.find_element(By.XPATH, "//input[@name='username']")
        username_textbox.send_keys(valid_username)
        password_textbox = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password_textbox.send_keys(invalid_password)
        self.driver.find_element(By.XPATH, "//button[text()='Sign In']").click()

        url_name = self.driver.current_url
        assert url_name == "https://groceryapp.uniqassosiates.com/admin/login"

    @pytest.mark.run(order=4)
    def test_login_with_invalid_password_and_invalid_username(self, browser_instance):
        self.driver = browser_instance
        excelutility = Excelutility()
        invalid_username = excelutility.read_user_data(5, 1)
        invalid_password = excelutility.read_user_data(5, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        username_textbox = self.driver.find_element(By.XPATH, "//input[@name='username']")
        username_textbox.send_keys(invalid_username)
        password_textbox = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password_textbox.send_keys(invalid_password)
        self.driver.find_element(By.XPATH, "//button[text()='Sign In']").click()

        url_name = self.driver.current_url
        assert url_name == "https://groceryapp.uniqassosiates.com/admin/login"


