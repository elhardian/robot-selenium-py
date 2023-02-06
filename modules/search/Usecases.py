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
        product_index = 0
        is_valid_price = True
        price_label = ""
        for element in elements:
            if element.text.startswith("Rp"):
                price = int(sub(r'Rp\.|[^\d.]', '', element.text))
                if price < min_amount or price > max_amount:
                    price_label=element.text
                    is_valid_price = False
                    break
            product_index+=1
        
        if not is_valid_price:
            properties_element = self.element_helper.get_elements_by_class_name(element_class_property_name)
            not_valid_property = properties_element[product_index]
            raise Exception(f"Property {not_valid_property.text} price is {price_label} which less than minimum or more than maximum")

