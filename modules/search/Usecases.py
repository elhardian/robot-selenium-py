import sys 
import os
import time
from re import sub
from selenium.webdriver.common.keys import Keys
current_directory = os.getcwd()
sys.path.append(current_directory)

from modules.search.Constants import *
from helpers.Elements import Element

class Usecases:
    element_helper = Element()

    def go_to_home_page(self):
        self.element_helper.go_to_page()

    def check_visibility_of_home_page(self):
        self.element_helper.get_element_by_class_name(element_class_home_visibility)
    
    def click_on_filter_button(self):
        input_search_element = self.element_helper.get_element_by_class_name(element_class_filter_button)
        input_search_element.click()

    def input_filter_minimum_amount(self, amount=filter_price_from):
        element = self.element_helper.get_element_by_id(element_id_input_filter_minimum_price)
        self.element_helper.double_click(element) # for clearing initial value / placeholder
        element.send_keys(amount)

    def input_filter_maximum_amount(self, amount=filter_price_to):
        element = self.element_helper.get_element_by_id(element_id_input_filter_maximum_price)
        element.send_keys(Keys.BACKSPACE)
        self.element_helper.double_click(element) # for clearing initial value / placeholder
        element.send_keys(amount)

    def submit_search_filter(self):
        element = self.element_helper.get_element_by_class_name(element_class_submit_search)
        element.click()

    def validate_price_on_search_result(self, min_amount=filter_price_from, max_amount=filter_price_to):
        time.sleep(5)
        elements = self.element_helper.get_elements_by_class_name(element_class_price_label)
        for element in elements:
            if element.text.startswith("Rp"):
                price = int(sub(r'Rp\.|[^\d.]', '', element.text))
                if price < min_amount or price > max_amount:
                    raise Exception(f"Some property price are out of filter range which is {element.text}")
                
        self.element_helper.quit_driver()