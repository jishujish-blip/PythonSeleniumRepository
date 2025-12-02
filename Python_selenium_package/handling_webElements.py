from selenium.webdriver.common.by import By

from Python_selenium_package.basic_selenium import Basics_selenium


class Handling_webelements(Basics_selenium):
    def verify_webelement_commands(self):
        self.driver.get("https://selenium.qabible.in/simple-form-demo.php")
        message_box = self.driver.find_element(By.XPATH, "// input[ @ id = 'single-input-field']")
        message_box.send_keys("test data")
        message_button = self.driver.find_element(By.XPATH, "//button[@id='button-one']")
        message_button.click()
        get_text_message = self.driver.find_element(By.XPATH, "// div[ @ id = 'message-one']")
        print(get_text_message.text)
        print(get_text_message.is_displayed())  ## By default is_displayed function is False
        print((get_text_message.is_enabled()))  ## By default is_displayed function is False
        message_box.clear()



obj1 = Handling_webelements()
obj1.initialize_browser()
obj1.verify_webelement_commands()
