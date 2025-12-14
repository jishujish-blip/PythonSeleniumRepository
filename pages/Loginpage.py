from selenium.webdriver.common.by import By


from utility.page_utility import PageUtility
from utility.wait_utitlity import Waitutility


class Loginpage:
    def __init__(self, driver):
        self.driver = driver
        self.wait_utility = Waitutility()
        self.pageutility = PageUtility()

    def enter_username(self, valid_username_value):
        user1 = self.driver.find_element(By.XPATH, "//input[@name='username']")
        # user1.send_keys(valid_username_value)
        self.pageutility.send_data_to_element(user1, valid_username_value)
        return self  # retuns login page

    def enter_password(self, valid_password_value):
        pass1 = self.driver.find_element(By.XPATH, "//input[@name='password']")
        # pass1.send_keys(valid_password_value)
        self.pageutility.send_data_to_element(pass1, valid_password_value)
        return self  # retuns login page

    def sign_in(self, driver):
        SignIn = self.driver.find_element(By.XPATH, "//button[text()='Sign In']")
        self.wait_utility.wait_until_clickable(self.driver, SignIn)
        # SignIn.click()
        self.pageutility.click_on_element(SignIn)
        from pages.Homepage import Homepage
        return Homepage(self.driver)         #chaining of classes





