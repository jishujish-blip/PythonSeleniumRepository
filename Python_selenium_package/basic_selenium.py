from selenium import webdriver
class Basics_selenium:
    def __init__(self):
        self.driver = None
    def initialize_browser(self):
        # self.driver=webdriver.Chrome()
        self.driver=webdriver.Firefox()
        self.driver.get("https://selenium.qabible.in/")
        self.driver.maximize_window()
    def close_browser(self):
        # self.driver.close()
        self.driver.quit()


if __name__ =="__main__":
    base = Basics_selenium()
    base.initialize_browser()
    base.close_browser()