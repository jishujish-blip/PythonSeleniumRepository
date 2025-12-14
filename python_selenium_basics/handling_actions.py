from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from python_selenium_basics.basic_selenium import Basics_selenium


class Handling_actions(Basics_selenium):
    def verify_mouse_hover(self):
        self.driver.get("https://selenium.qabible.in/simple-form-demo.php")
        home_text=self.driver.find_element(By.XPATH,"//a[text()='Home']")
        actions=ActionChains(self.driver)   # class provided by selenium. Useful to easily simulate mouse actions and keyboard actions
        actions.move_to_element(home_text).perform()
        print(home_text.text)  #print HOME text

    def verify_right_click(self):
        home_text = self.driver.find_element(By.XPATH, "//a[text()='Home']")
        actions = ActionChains(self.driver)
        actions.context_click(home_text).perform()

    def verify_drag_and_drop(self):
        self.driver.get("https://demoqa.com/droppable")
        drag_me=self.driver.find_element(By.XPATH,"// div[@id='simpleDropContainer']/div[1][@id='draggable'][text()='Drag me']")

        drop_me=self.driver.find_element(By.XPATH,"//div[@id='simpleDropContainer']/div[2][@id='droppable']/p[text()='Drop here']")
        actions = ActionChains(self.driver)
        actions.drag_and_drop(drag_me, drop_me).perform()

    def verify_keyboard_action(self):
        # Simulate pressing Ctrl + T to open a new tab (using pyautogui)
        pyautogui.hotkey('ctrl', 't')
        time.sleep(2)  # Adding delay for visibility
        pyautogui.write('https://www.google.com')  # Typing URL
        pyautogui.press('enter')  # Pressing Enter


handle_action= Handling_actions()
handle_action.initialize_browser()
handle_action.verify_mouse_hover()
handle_action.verify_right_click()
handle_action.verify_drag_and_drop()