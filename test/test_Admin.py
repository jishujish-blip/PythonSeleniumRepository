import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.Adminpage import Adminpage
from pages.Loginpage import Loginpage
from utility.Excelutility import Excelutility


class TestAdmin:
    def test_return_to_home(self, browser_instance):
        self.driver = browser_instance
        excel_utility = Excelutility()
        valid_username = excel_utility.read_user_data(2, 1)
        valid_password = excel_utility.read_user_data(2, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")

        loginpage = Loginpage(self.driver)
        # loginpage.enter_username(valid_username)
        # loginpage.enter_password(valid_password)
        loginpage.enter_username(valid_username).enter_password(valid_password)
        homepage = loginpage.sign_in(self.driver)

        # adminpage=Adminpage(self.driver)

        adminpage = homepage.list_admin(self.driver)
        homepage = adminpage.go_home_page(self.driver)

        home_url = self.driver.current_url
        assert home_url == "https://groceryapp.uniqassosiates.com/admin/home"

    def test_create_new_user(self, browser_instance):
        self.driver = browser_instance
        excel_utility = Excelutility()
        valid_username = excel_utility.read_user_data(2, 1)
        valid_password = excel_utility.read_user_data(2, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")

        loginpage = Loginpage(self.driver)
        # loginpage.enter_username(valid_username)
        # time.sleep(1)
        # loginpage.enter_password(valid_password)
        # time.sleep(1)
        loginpage.enter_username(valid_username).enter_password(valid_password)
        homepage = loginpage.sign_in(self.driver)
        time.sleep(1)

        #adminpage = Adminpage(self.driver)
        adminpage = homepage.list_admin(self.driver)
        time.sleep(1)
        adminpage.newbutton(self.driver)
        # adminpage.input_new_user(self.driver)
        # time.sleep(1)
        # adminpage.input_new_user_password(self.driver)
        adminpage.input_new_user(self.driver).input_new_user_password(self.driver)
        time.sleep(1)
        adminpage.user_type_dropdown(self.driver)
        time.sleep(1)
        adminpage = adminpage.create_admin(self.driver)
        time.sleep(1)

        alert = self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")
        alert_text = alert.text.strip()

        expected_messages = [
            "Username already exists.",
            "User Created Successfully"
        ]
        assert any(msg in alert_text for msg in expected_messages), \
            f"Unexpected alert message: {alert_text}"

    def test_search_user(self, browser_instance):
        self.driver = browser_instance
        excel_utility = Excelutility()
        valid_username = excel_utility.read_user_data(2, 1)
        valid_password = excel_utility.read_user_data(2, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")

        loginpage = Loginpage(self.driver)
        # loginpage.enter_username(valid_username)
        # time.sleep(1)
        # loginpage.enter_password(valid_password)
        loginpage.enter_username(valid_username).enter_password(valid_password)
        time.sleep(1)
        homepage = loginpage.sign_in(self.driver)
        time.sleep(1)

        #adminpage = Adminpage(self.driver)
        adminpage=homepage.list_admin(self.driver)
        time.sleep(1)
        adminpage = adminpage.click_admin_search_button(self.driver)
        time.sleep(1)
        # adminpage.search_admin_user_in_textbox(self.driver)
        # time.sleep(1)
        # adminpage.select_user_type_dropdown(self.driver)
        adminpage.search_admin_user_in_textbox(self.driver).select_user_type_dropdown(self.driver).click_search_button(
            self.driver)
        # time.sleep(1)
        # adminpage.click_search_button(self.driver)
        time.sleep(1)

    def test_reset_admin_user_page(self, browser_instance):
        self.driver = browser_instance
        excel_utility = Excelutility()
        valid_username = excel_utility.read_user_data(2, 1)
        valid_password = excel_utility.read_user_data(2, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        loginpage = Loginpage(self.driver)
        # loginpage.enter_username(valid_username)
        # time.sleep(1)
        # loginpage.enter_password(valid_password)
        # time.sleep(1)
        loginpage.enter_username(valid_username).enter_password(valid_password)
        time.sleep(1)
        homepage = loginpage.sign_in(self.driver)
        time.sleep(1)

        #adminpage = Adminpage(self.driver)
        adminpage=homepage.list_admin(self.driver)
        time.sleep(1)
        adminpage = adminpage.reset_admin(self.driver)

        admin_url = self.driver.current_url
        assert admin_url == "https://groceryapp.uniqassosiates.com/admin/list-admin"
