import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class login_details:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
        self.username=(By.CSS_SELECTOR,"input[name='user-name']")
        self.password=(By.CSS_SELECTOR,"input[name='password']")
        self.click_login_button=(By.ID,"login-button")


    def enter_login_details(self,user,pass_1):
        username=self.wait.until(EC.presence_of_element_located(self.username))
        username.send_keys(user)
        password=self.wait.until(EC.presence_of_element_located(self.password))
        password.send_keys(pass_1)
        login_button=self.wait.until(EC.element_to_be_clickable(self.click_login_button))
        login_button.click()

