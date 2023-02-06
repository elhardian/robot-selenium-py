from Setting import chrome_driver as driver, capture_on_error
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidSessionIdException
from selenium.webdriver.common.action_chains import ActionChains
import sys 
import os
current_directory = os.getcwd()
sys.path.append(current_directory)

class Element:
    element_timeout = 30
    base_url = os.environ.get('BASE_URL', 'https://airbnb.com')

    def go_to_page(self, path=""):
        destination_page = self.base_url + path
        driver.get(destination_page)

    def get_element_by_data_automation(self, automation_id):
        try:
            element = WebDriverWait(driver, self.element_timeout).until(
                EC.element_to_be_clickable((By.XPATH, f"//*[@data-automation='{automation_id}']"))
            )
            return element
        except InvalidSessionIdException:
            if capture_on_error: self.__take_a_screenshot()
            self.quit_driver()
            raise Exception(f"element with data-automation *{automation_id}* couldn't be found after waiting {self.element_timeout} seconds")
        
    def get_element_by_id(self, element_id):
        try:
            element = WebDriverWait(driver, self.element_timeout).until(
                EC.element_to_be_clickable((By.ID, element_id))
            )
            return element
        except:
            if capture_on_error: self.__take_a_screenshot()
            self.quit_driver()
            raise Exception(f"element with id *{element_id}* couldn't be found after waiting {self.element_timeout} seconds")
        
    def get_element_by_class_name(self, class_name):
        try:
            element = WebDriverWait(driver, self.element_timeout).until(
                EC.element_to_be_clickable((By.CLASS_NAME, class_name))
            )
            return element
        except:
            if capture_on_error: self.__take_a_screenshot()
            self.quit_driver()
            raise Exception(f"element with class *{class_name}* couldn't be found after waiting {self.element_timeout} seconds")
    
    def get_elements_by_class_name(self, class_name):
        try:
            elements = driver.find_elements_by_class_name(class_name)
            return elements
        except:
            if capture_on_error: self.__take_a_screenshot()
            self.quit_driver()
            raise Exception(f"elements with class *{class_name}* couldn't be found after waiting {self.element_timeout} seconds")
        
    def double_click(self, element):
        actionChains = ActionChains(driver)
        actionChains.double_click(element).perform()

    def quit_driver(self):
        driver.quit()
        
    def __take_a_screenshot(self):
        driver.save_screenshot(f"failed.png")