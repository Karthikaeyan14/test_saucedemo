import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

class admin:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
        self.dropdown=(By.CLASS_NAME,"product_sort_container")
        self.total_product=(By.CLASS_NAME,"inventory_item ")
        self.add_cart_button=(By.XPATH,"//button[text()='Add to cart']")
        #self.add_cart_1=(By.XPATH,"//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
        #self.add_cart_2=(By.XPATH,"//button[@id='add-to-cart-sauce-labs-onesie']")
        #self.add_cart_button=(By.CSS_SELECTOR,"button[class='btn btn_primary btn_small btn_inventory']")
        self.cart_icon=(By.XPATH,"//span[@class='shopping_cart_badge']")
        self.cart=(By.CLASS_NAME,"shopping_cart_badge")
        self.checkbout_button=(By.ID,"checkout")
        self.first_name=(By.ID,"first-name")
        self.last_name=(By.ID,"last-name")
        self.pin_code=(By.ID,"postal-code")
        self.process=(By.ID,"continue")
        self.Payment_info=(By.XPATH,"//div[@data-test='payment-info-value']")
        self.finish=(By.XPATH,"//button[text()='Finish']")


    def method(self):
        title=self.driver.title
        print("Title is:",title)
        add_cart=self.wait.until(EC.element_to_be_clickable(self.dropdown))
        add_cart.click()
        select_dropdown=Select(add_cart)
        select_dropdown.select_by_index(1)
        #inital_cart_icon=self.wait.until(EC.visibility_of_element_located(self.cart_icon)).text
        Total_product=self.wait.until(EC.presence_of_all_elements_located(self.total_product))
        Total_product_count=len(Total_product)
        print("Total Product Count is:",Total_product_count)
        
        """
        select_product_1=self.wait.until(EC.element_to_be_clickable(self.add_cart_1))
        add=0
        select_product_1.click()
        cart_icon = self.wait.until(EC.visibility_of_element_located(self.cart_icon)).text
        print(cart_icon)

        assert int(cart_icon)==1
        add=add+1

        select_product_2=self.wait.until(EC.element_to_be_clickable(self.add_cart_2))
        select_product_2.click()

        
        add=add+1

        print("Add Product is:",add)
        """
        count=len(self.add_cart_button)   
        time.sleep(2)     
        print("Total cart Count is:",count)
        
        for i in range(count):
            cart_click=self.wait.until(EC.element_to_be_clickable(self.add_cart_button))
            cart_click.click()
        cart_icon=self.wait.until(EC.visibility_of_element_located(self.cart_icon)).text
        
        #assert int(cart_icon)==2
        

    def checkout(self):
        cart=self.wait.until(EC.element_to_be_clickable(self.cart))
        cart.click()
        title=self.driver.title
        print("Title of page:",title)
        checkout=self.wait.until(EC.element_to_be_clickable(self.checkbout_button))
        checkout.click()

        first_name=self.wait.until(EC.presence_of_element_located(self.first_name))
        first_name.send_keys("karthi")
        last_name=self.wait.until(EC.presence_of_element_located(self.last_name))
        last_name.send_keys("r")
        pin_code=self.wait.until(EC.presence_of_element_located(self.pin_code))
        pin_code.send_keys("613001")
        cont=self.wait.until(EC.element_to_be_clickable(self.process))
        cont.click()

    def processed(self):
        pay_info=self.wait.until(EC.presence_of_element_located(self.Payment_info)).text
        pay_infomation=str(pay_info)
        print(pay_infomation)
        finish=self.wait.until(EC.element_to_be_clickable(self.finish))
        finish.click()







