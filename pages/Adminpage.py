from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



from utility.page_utility import PageUtility
from utility.wait_utitlity import Waitutility


class Adminpage:
    def __init__(self, driver):
        self.driver = driver
        self.wait_utility = Waitutility()
        self.page_utility = PageUtility()



    def go_home_page(self, driver):
        home_link = self.driver.find_element(By.XPATH, "//a[text()='Home']")
        # home_link.click()
        self.page_utility.click_on_element(home_link)
        from pages.Homepage import Homepage
        return Homepage(self.driver)

    def newbutton(self, driver):
        new_button = self.driver.find_element(By.XPATH, "//a[@onclick='click_button(1)']")
        # new_button.click()
        self.page_utility.click_on_element(new_button)
        return self

    def input_new_user(self, text):
        new_user_textbox = self.driver.find_element(By.XPATH, "//input[@id='username']")
        # new_user_textbox.send_keys("my_name")
        self.page_utility.send_data_to_element(new_user_textbox, "my_name")
        return self

    def input_new_user_password(self, text):
        new_password_textbox = self.driver.find_element(By.XPATH, "//input[@id='password']")
        # new_password_textbox.send_keys("my_password")
        self.page_utility.send_data_to_element(new_password_textbox, "my_password")
        return self

    def user_type_dropdown(self, driver):
        userType_dropdown = self.driver.find_element(By.XPATH, "//select[@id='user_type']")
        # select = Select(userType_dropdown)
        # select.select_by_visible_text("Staff")
        self.page_utility.select_data_with_value(userType_dropdown, "Staff")
        return self

    def create_admin(self, driver):
        new_admin = self.driver.find_element(By.XPATH, "//button[@name='Create']")
        # new_admin.click()
        self.page_utility.click_on_element(new_admin)
        return self

    def reset_admin(self, driver):
        reset = self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-warning']")
        # reset.click()
        self.page_utility.click_on_element(reset)
        return self

    def click_admin_search_button(self, driver):
        admin_search_button = self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-primary']")
        # admin_search_button.click()
        self.page_utility.click_on_element(admin_search_button)
        return self

    def search_admin_user_in_textbox(self, text):
        admin_textbox = self.driver.find_element(By.XPATH, "//input[@id='un']")
        # admin_textbox.send_keys("my_user")
        self.page_utility.send_data_to_element(admin_textbox, "my_user")
        return self

    def select_user_type_dropdown(self, driver):
        user_type_dropdown = self.driver.find_element(By.XPATH, "//select[@id='ut']")
        # select = Select(user_type_dropdown)
        # select.select_by_visible_text("Staff")
        self.page_utility.select_data_with_value(user_type_dropdown, "Staff")
        return self

    def click_search_button(self, button):
        search_button = self.driver.find_element(By.XPATH, "//button[@name='Search']")
        # search_button.click()
        self.page_utility.click_on_element(search_button)
        return self

