import time

import pytest
from selenium.webdriver.common.by import By

from pages.Loginpage import Loginpage

from utility.Excelutility import Excelutility


class TestManage_news:
    def test_manage_news(self, browser_instance):
        self.driver = browser_instance
        excel_utility = Excelutility()
        valid_username = excel_utility.read_user_data(2, 1)
        valid_password = excel_utility.read_user_data(2, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(valid_username).enter_password(valid_password)
        homepage=loginpage.sign_in(self.driver)
        # loginpage.enter_password(valid_password)
        # loginpage.sign_in(self.driver)
        time.sleep(1)

        #managenews = Managenews(self.driver)
        managenews=homepage.click_manage_news(self.driver)
        managenews.click_new_news_button(self.driver).enter_new_news(self.driver).save_new_news(self.driver)
        # managenews.click_new_news_button(self.driver)
        # time.sleep(1)
        # managenews.enter_new_news(self.driver)
        # time.sleep(1)
        # managenews.save_new_news(self.driver)

        alert_message = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
        assert "News Created Successfully" in alert_message.text

    def test_search_news(self, browser_instance):
        self.driver = browser_instance
        excel_utility = Excelutility()
        valid_username = excel_utility.read_user_data(2, 1)
        valid_password = excel_utility.read_user_data(2, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        loginpage = Loginpage(self.driver)
        loginpage.enter_username(valid_username).enter_password(valid_password)
        homepage=loginpage.sign_in(self.driver)
        # loginpage.enter_password(valid_password)
        # loginpage.sign_in(self.driver)
        time.sleep(1)

        #managenews = Managenews(self.driver)
        managenews=homepage.click_manage_news(self.driver)
        managenews.click_search_news_button(self.driver).enter_the_search_news_title(self.driver).click_search_button_after_entering_news_title(self.driver)
        # time.sleep(1)
        # managenews.click_search_news_button(self.driver)
        # managenews.enter_the_search_news_title(self.driver)
        # managenews.click_search_button_after_entering_news_title(self.driver)
        time.sleep(2)

        row_data = self.driver.find_element(By.XPATH,
                                            "//table[@class='table table-bordered table-hover table-sm']/tbody/tr/td")
        assert "Its snowing!!!" not in row_data.text
