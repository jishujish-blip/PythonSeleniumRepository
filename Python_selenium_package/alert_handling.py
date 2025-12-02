#simple alert - only OK button
#confirm alert -OK and Cancel button
#Prompt alert- Take input from user for decision
import time

from selenium.webdriver.common.by import By

from Python_selenium_package.basic_selenium import Basics_selenium


class Alert_handling(Basics_selenium):
    # def verify_simple_alert(self):
    #     self.driver.get("https://demoqa.com/alerts")
    #     simple_alert_button=self.driver.find_element(By.XPATH,"//button[@id='alertButton']")
    #     simple_alert_button.click()
    #     # Switch to alert and accept it
    #     alert = self.driver.switch_to.alert
    #     alert_text = alert.text
    #     print(alert_text)
    #     alert.accept()
    #     time.sleep(10)
    # def verify_confirm_alert(self):
    #     self.driver.get("https://demoqa.com/alerts")
    #     confirm_alert_button=self.driver.find_element(By.XPATH,"//button[@id='confirmButton']")
    #     confirm_alert_button.click()
    #     alert=self.driver.switch_to.alert
    #     alert.accept()
    #     alert_text_returned = self.driver.find_element(By.XPATH, "//span[@id='confirmResult']")
    #     print(alert_text_returned.text)
    #     time.sleep(10)
    def verify_promt_alert(self):
        self.driver.get("https://demoqa.com/alerts")
        promt_button=self.driver.find_element(By.XPATH,"//button[@id='promtButton']")
        promt_button.click()
        alert=self.driver.switch_to.alert
        alert.send_keys("Go Ahead")
        alert.accept()
        time.sleep(10)




alert_handle=Alert_handling()
alert_handle.initialize_browser()
# alert_handle.verify_simple_alert()
# alert_handle.verify_confirm_alert()
alert_handle.verify_promt_alert()