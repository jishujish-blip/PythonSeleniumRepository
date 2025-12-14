import string
import random

import pytest
from selenium.webdriver.common.by import By

from pages.Loginpage import Loginpage
from utility.Excelutility import Excelutility


def generate_random_username():
    return "user_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))


class Test_login:
   #@pytest.mark.smoke
    @pytest.mark.run(order=1)
    def test_login_with_valid_credentials(self, browser_instance):
        self.driver = browser_instance  # webdriver instance is holding browser_instance
        # driver is local variable in browser_instance function
        excelutility = Excelutility()
        valid_username_value = excelutility.read_user_data(2, 1)  # username value form excel sheet
        valid_password_value = excelutility.read_user_data(2, 2)  # password value form excel sheet
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        self.driver.implicitly_wait(5)

        loginpage = Loginpage(self.driver)
        loginpage.enter_username(valid_username_value).enter_password(
            valid_password_value)  # chaining of functions/methods
        # loginpage.enter_password(valid_password_value)
        homepage= loginpage.sign_in(self.driver)

        url_name = self.driver.current_url
        assert url_name == "https://groceryapp.uniqassosiates.com/admin"

    @pytest.mark.run(order=2)
    def test_login_with_invalid_username(self, browser_instance):
        self.driver = browser_instance
        excelutility = Excelutility()
        invalid_username = excelutility.read_user_data(4, 1)
        valid_password = excelutility.read_user_data(4, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(invalid_username).enter_password(valid_password).sign_in(self.driver)

        #loginpage.enter_password(valid_password)
        #loginpage.sign_in(self.driver)

        url_name = self.driver.current_url
        assert url_name == "https://groceryapp.uniqassosiates.com/admin/login"

    @pytest.mark.parametrize("username_value", ["user1", "user2", "user3"])
    # @pytest.mark.parametrize("username_value",  [generate_random_username()])  #parametrization using single testdata
    @pytest.mark.run(order=3)
    def test_login_with_invalid_password(self, browser_instance, username_value):
        self.driver = browser_instance
        excelutility = Excelutility()
        # valid_username = excelutility.read_user_data(3, 1)

        invalid_password = excelutility.read_user_data(3, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(username_value).enter_password(invalid_password).sign_in(self.driver)

        # loginpage.enter_password(invalid_password)
        # loginpage.sign_in(self.driver)

        url_name = self.driver.current_url
        assert url_name == "https://groceryapp.uniqassosiates.com/admin/login"

    @pytest.mark.run(order=4)
    def test_login_with_invalid_password_and_invalid_username(self, browser_instance):
        self.driver = browser_instance
        excelutility = Excelutility()
        invalid_username = excelutility.read_user_data(5, 1)
        invalid_password = excelutility.read_user_data(5, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        self.driver.implicitly_wait(5)
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(invalid_username).enter_password(invalid_password).sign_in(self.driver)

        # loginpage.enter_password(invalid_password)
        # loginpage.sign_in(self.driver)

        url_name = self.driver.current_url
        assert url_name == "https://groceryapp.uniqassosiates.com/admin/login"
