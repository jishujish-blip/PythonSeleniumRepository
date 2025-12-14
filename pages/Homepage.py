from selenium.webdriver.common.by import By

from pages.Managenews import Managenews
from utility.page_utility import PageUtility
from utility.wait_utitlity import Waitutility


class Homepage:
    def __init__(self, driver):
        self.driver = driver
        self.page_utility = PageUtility()
        self.wait_utility = Waitutility()

    def list_admin(self, driver):
        list_admin = self.driver.find_element(By.XPATH,
                                              "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer'] ")
        self.wait_utility.wait_until_clickable(self.driver, list_admin)
        # list_admin.click()
        self.page_utility.click_on_element(list_admin)
        from pages.Adminpage import Adminpage
        return Adminpage(self.driver)

    def click_manage_news(self, driver):
        manage_news_button = self.driver.find_element(By.XPATH,
                                                      "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news']")
        # manage_news_button.click()
        self.page_utility.click_on_element(manage_news_button)
        return Managenews(self.driver)

    def click_admin_to_logout(self, driver):
        admin_logout = self.driver.find_element(By.XPATH, "//li[@class='nav-item dropdown']")
        # admin_logout.click()
        self.page_utility.click_on_element(admin_logout)
        from pages.Loginpage import Loginpage
        return Loginpage(self.driver)

    def logout_from_home_page(self, driver):
        logout_link = self.driver.find_element(By.XPATH, "//a/i[@class='ace-icon fa fa-power-off']")
        # logout_link.click()
        self.page_utility.click_on_element(logout_link)
        from pages.Loginpage import Loginpage
        return Loginpage(self.driver)
