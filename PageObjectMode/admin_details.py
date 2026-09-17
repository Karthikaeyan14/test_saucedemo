from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


class admin:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.dropdown = (By.CLASS_NAME, "product_sort_container")
        self.product_cards = (By.CLASS_NAME, "inventory_item")
        self.add_cart_button = (By.XPATH, "//button[contains(@class, 'btn_inventory') and text()='Add to cart']")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")
        self.checkout_button = (By.ID, "checkout")
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.pin_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.payment_info = (By.XPATH, "//div[@data-test='payment-info-value']")
        self.finish_button = (By.XPATH, "//button[text()='Finish']")
        self.login_error = (By.XPATH, "//h3[@data-test='error']")


    def sort_products(self):
        dropdown = self.wait.until(EC.element_to_be_clickable(self.dropdown))
        dropdown.click()
        select_dropdown = Select(dropdown)
        select_dropdown.select_by_index(1)
        return self

    def add_all_products_to_cart(self):
        product_buttons = self.wait.until(EC.presence_of_all_elements_located(self.add_cart_button))
        for button in product_buttons:
            if button.is_displayed():
                button.click()
        return self.get_cart_count()

    def get_cart_count(self):
        cart_badge = self.driver.find_elements(*self.cart_badge)
        if not cart_badge:
            return 0
        return int(cart_badge[0].text) if cart_badge[0].text else 0

    def method(self):
        """Open the product listing, sort it, and add all available products to the cart."""
        self.sort_products()
        total_products = self.wait.until(EC.presence_of_all_elements_located(self.product_cards))
        print("Total Product Count is:", len(total_products))
        cart_count = self.add_all_products_to_cart()
        print("Total cart Count is:", cart_count)
        return cart_count

    def checkout(self):
        cart = self.wait.until(EC.element_to_be_clickable(self.cart_button))
        cart.click()
        print("Title of page:", self.driver.title)

        checkout = self.wait.until(EC.element_to_be_clickable(self.checkout_button))
        checkout.click()

        first_name = self.wait.until(EC.presence_of_element_located(self.first_name))
        first_name.send_keys("karthi")

        last_name = self.wait.until(EC.presence_of_element_located(self.last_name))
        last_name.send_keys("r")

        pin_code = self.wait.until(EC.presence_of_element_located(self.pin_code))
        pin_code.send_keys("613001")

        continue_button = self.wait.until(EC.element_to_be_clickable(self.continue_button))
        continue_button.click()
        return self

    def processed(self):
        payment_info = self.wait.until(EC.presence_of_element_located(self.payment_info)).text
        print(payment_info)

        finish = self.wait.until(EC.element_to_be_clickable(self.finish_button))
        finish.click()
        return self
    
    def error_message(self):
        error_message = self.wait.until(EC.visibility_of_element_located(self.login_error)).text
        #print(error_message)
        return error_message
    
    def customer_detail(self):
        cart = self.wait.until(EC.element_to_be_clickable(self.cart_button))
        cart.click()   
        checkout = self.wait.until(EC.element_to_be_clickable(self.checkout_button))
        checkout.click()
         
        continue_button = self.wait.until(EC.element_to_be_clickable(self.continue_button))
        continue_button.click()
        
        print(self.error_message())
        
            


# Backward-compatible alias used by the current tests.
AdminPage = admin







