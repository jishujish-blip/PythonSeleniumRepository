from selenium.webdriver.common.by import By

from python_selenium_basics.basic_selenium import Basics_selenium


class HandlingFrames(Basics_selenium):
    def verify_frames(self):
        self.driver.get("https://demoqa.com/frames")
        # Find all iframe elements
        total_frames = self.driver.find_elements(By.TAG_NAME, "iframe")
        # Print the number of frames
        print(len(total_frames))
        frame1=self.driver.find_element(By.XPATH,"//iframe[@id='frame1']")
        #switching the focus
        self.driver.switch_to.frame('frame1')
        frame_text=self.driver.find_element(By.XPATH,"//h1[@id='sampleHeading']")
        print(frame_text.text)
        #releasing the focus form current frame
        self.driver.switch_to.default_content()

frames = HandlingFrames()
frames.initialize_browser()
frames.verify_frames()