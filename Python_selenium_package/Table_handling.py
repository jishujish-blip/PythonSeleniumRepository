from selenium.webdriver.common.by import By

from Python_selenium_package.basic_selenium import Basics_selenium


class Table_handling(Basics_selenium):
    def handle_tables(self):
        self.driver.get("https://money.rediff.com/indices/nse")
        table_variable = self.driver.find_element(By.XPATH, "//table[@id='dataTable']")
        print(table_variable.text)
        table_row = self.driver.find_element(By.XPATH, "//table[@id='dataTable']/tbody/tr[3]")
        print("Third row text is ", table_row.text)  # Get the text of the row
        table_column= self.driver.find_element(By.XPATH, "//table[@id='dataTable']/tbody/tr[3]/td[2]")
        print("Third row second column text is ", table_column.text)  # Get the text of the third row second column

        # receive lasrt element in a table row
        table_last_row=self.driver.find_element(By.XPATH, "//table[@id='dataTable']/tbody/tr[last()]")
        print("Last row of table is ", table_last_row.text)
        #3rd row last column
        third_row_last_column=self.driver.find_element(By.XPATH, "//table[@id='dataTable']/tbody/tr[3]/td[last()]")
        print("Third row last column of table is ", third_row_last_column.text)

        #lastrow last column
        #//table[@id='dataTable']/tbody/tr[last()]/td[last()]

        # find_elements in Selenium is used to locate multiple elements on a webpage that match the same locator.
        # It returns a list of WebElements
table_handle = Table_handling()
table_handle.initialize_browser()
table_handle.handle_tables()
