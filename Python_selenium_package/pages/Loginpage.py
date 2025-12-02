from selenium.webdriver.common.by import By


class Loginpage:
    def __init__(self,driver):
        self.driver=driver
    def enter_username(self,valid_username_value):
        self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(valid_username_value)
    def enter_password(self,valid_password_value):
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(valid_password_value)
    def sign_in(self,driver):
        self.driver.find_element(By.XPATH, "//button[text()='Sign In']").click()

