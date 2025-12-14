import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.Homepage import Homepage
from pages.Loginpage import Loginpage
from utility.Excelutility import Excelutility


class Test_HomeTest:
    # @pytest.mark.timeout(10)
    def test_logout(self,cross_browser):
        self.driver=cross_browser
        excel_utility=Excelutility()
        valid_username=excel_utility.read_user_data(2,1)
        valid_password=excel_utility.read_user_data(2,2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")

        loginpage = Loginpage(self.driver)
        # loginpage.enter_username(valid_username)
        # time.sleep(1)
        # loginpage.enter_password(valid_password)
        # time.sleep(1)
        # loginpage.sign_in(self.driver)
        # time.sleep(1)
        loginpage.enter_username(valid_username).enter_password(
            valid_password)  # chaining of functions/methods
        # loginpage.enter_password(valid_password_value)
        homepage= loginpage.sign_in(self.driver)
        #homepage=Homepage(self.driver)      #above signin step already returned homepage and there is no need to create an object for Homepage
        homepage.click_admin_to_logout(self.driver)
        time.sleep(3)
        loginpage=homepage.logout_from_home_page(self.driver)   #logged out from homepage and returned loginpage(object name)
        time.sleep(2)

