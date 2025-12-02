from Python_selenium_package.basic_selenium import Basics_selenium


class Handle_browser_commands(Basics_selenium):
    def verify_commands(self):
        title = self.driver.title
        print(title)
        url=self.driver.current_url
        print(url)
        handle_id=self.driver.current_window_handle
        print(handle_id)


obj1 = Handle_browser_commands()
obj1.initialize_browser()
obj1.verify_commands()
obj1.close_browser()

