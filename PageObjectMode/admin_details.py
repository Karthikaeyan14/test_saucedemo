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
        self.cost=(By.CLASS_NAME, "inventory_item_price")
        self.checkout_button = (By.ID, "checkout")
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.pin_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.payment_info = (By.XPATH, "//div[@data-test='payment-info-value']")
        self.finish_button = (By.XPATH, "//button[text()='Finish']")
        self.login_error = (By.XPATH, "//h3[@data-test='error']")
        self.remove_product_cart = (By.XPATH, "//button[text()='Remove']")
        self.total_price_details=(By.CLASS_NAME, "summary_subtotal_label")
        self.summary_total_details=(By.CLASS_NAME, "summary_total_label")


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
    
    def get_product_costs(self):
        product_costs = self.wait.until(EC.presence_of_all_elements_located(self.cost))
        costs = [cost.text for cost in product_costs]
        return costs

    def method(self):
        """Open the product listing, sort it, and add all available products to the cart."""
        self.sort_products()
        total_products = self.wait.until(EC.presence_of_all_elements_located(self.product_cards))
        print("Total Product Count is:", len(total_products))
        cart_count = self.add_all_products_to_cart()
        print("Total cart Count is:", cart_count)
        return cart_count

    def remove_product_from_cart(self):
        initial_cart_count = self.get_cart_count()
        if initial_cart_count == 0:
            raise ValueError("Cannot remove a product from an empty cart")

        cart = self.wait.until(EC.element_to_be_clickable(self.cart_button))
        cart.click()

        #remove_button = self.wait.until(EC.element_to_be_clickable(self.remove_product_cart))
        #remove_button.click()
        for button in self.driver.find_elements(*self.remove_product_cart):
           button.click()
           #expected_cart_count = initial_cart_count - 1
        
        cart_count_after_removal = self.get_cart_count()
        print("Cart count after removal is:", cart_count_after_removal)   
       
    def cart_details(self):
        cart = self.wait.until(EC.element_to_be_clickable(self.cart_button))
        cart.click()
        print("Title of page:", self.driver.title)

        checkout = self.wait.until(EC.element_to_be_clickable(self.checkout_button))
        checkout.click()
    def checkout(self,f_n,l_n,pc):
        first_name = self.wait.until(EC.presence_of_element_located(self.first_name))
        first_name.send_keys(f_n)

        last_name = self.wait.until(EC.presence_of_element_located(self.last_name))
        last_name.send_keys(l_n)

        pin_code = self.wait.until(EC.presence_of_element_located(self.pin_code))
        pin_code.send_keys(pc)

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
    
    def price_details(self):
        
        #self.method()
        cart = self.wait.until(EC.element_to_be_clickable(self.cart_button))
        cart.click()
        print("Title of page:", self.driver.title)
        cost_details = self.wait.until(EC.presence_of_all_elements_located(self.cost))
        self.intial_amount=0
        for price in cost_details:
            prices=price.text.replace("$", "")
            cost_price=float(prices)
            self.intial_amount=self.intial_amount + cost_price
           
            #prices=float(price)+float(prices)
            
            #print(type(intial_amount))
        print(self.intial_amount)
        
        checkout = self.wait.until(EC.element_to_be_clickable(self.checkout_button))
        checkout.click()
        
     #tax_percentage= 8% so 0.08   
    def summary_total(self):
        total_Price=self.wait.until(EC.presence_of_element_located(self.total_price_details)).text
        total_Price=total_Price.replace("Item total: $", "")
        total_Price=float(total_Price)
        print("Total Price is:",total_Price)
        
        assert self.intial_amount ==total_Price, f"Expected total price {self.intial_amount}, but got {total_Price}"
        total_amount=total_Price + (total_Price * 0.08)
        total_amount=round(total_amount, 2)
        #print("Total Amount with tax is:",total_amount)
        
        summary_total=self.wait.until(EC.presence_of_element_located(self.summary_total_details)).text
        summary_total=summary_total.replace("Total: $", "")
        summary_total=float(summary_total)
        #print("Summary Total is:",summary_total)
        
        assert total_amount ==summary_total, f"Expected summary total {total_amount}, but got {summary_total}"


# Backward-compatible alias used by the current tests.
AdminPage = admin







