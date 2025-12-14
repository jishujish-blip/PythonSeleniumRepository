from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from python_selenium_basics.basic_selenium import Basics_selenium


class Handle_dropdowns(Basics_selenium):
    def verify_dropdowns(self):
        self.driver.get("https://www.webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
        dropdown1 = self.driver.find_element(By.XPATH, "//select[@id='dropdowm-menu-1']")
        select = Select(dropdown1)
        # select.select_by_index(1)
        # select.select_by_value("python")
        select.select_by_visible_text("SQL")
        self.driver.back()
        self.driver.forward()
        self.driver.refresh()

    def verify_checkbox(self):
        self.driver.get("https://www.webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
        check_box_variable = self.driver.find_element(By.XPATH, "//input[@value='option-1']")
        check_box_variable.click()
        print(check_box_variable.is_selected())
    def verify_radio_button(self):
        self.driver.get("https://www.webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
        radio_button_variable=self.driver.find_element(By.XPATH,"//input[@value='green']")
        radio_button_variable.click()

handle_dropdown = Handle_dropdowns()
handle_dropdown.initialize_browser()
handle_dropdown.verify_dropdowns()
handle_dropdown.verify_checkbox()
handle_dropdown.verify_radio_button()
