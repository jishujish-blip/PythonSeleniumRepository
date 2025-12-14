from selenium.webdriver.common.by import By

from utility.page_utility import PageUtility


class Managenews:
    def __init__(self, driver):
        self.driver = driver
        self.page_utility = PageUtility()

    def click_new_news_button(self, driver):
        new_news_button = self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-danger']")
        # new_news_button.click()
        self.page_utility.click_on_element(new_news_button)
        return self

    def enter_new_news(self, text):
        new_news_textbox = self.driver.find_element(By.XPATH, "//textarea[@name='news']")
        # new_news_textbox.send_keys("Its Snowing out here")
        self.page_utility.send_data_to_element(new_news_textbox, "Its Snowing out here")
        return self

    def save_new_news(self, driver):
        save_news = self.driver.find_element(By.XPATH, "// button[ @ name = 'create']")
        # save_news.click()
        self.page_utility.click_on_element(save_news)
        return self

    def click_search_news_button(self, driver):
        search_news_button = self.driver.find_element(By.XPATH, "//a[@onclick='click_button(2)']")
        # search_news_button.click()
        self.page_utility.click_on_element(search_news_button)
        return self

    def enter_the_search_news_title(self, text):
        search_news_title = self.driver.find_element(By.XPATH, "//input[@type='text']")
        # search_news_title.send_keys("Its Snowing out here")
        self.page_utility.send_data_to_element(search_news_title, "Its Snowing out here")
        return self

    def click_search_button_after_entering_news_title(self, driver):
        search_button = self.driver.find_element(By.XPATH, "// button[ @ name = 'Search']")
        # search_button.click()
        self.page_utility.click_on_element(search_button)
        return self
