from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username_field = (By.CSS_SELECTOR, "input[name='user-name']")
        self.password_field = (By.CSS_SELECTOR, "input[name='password']")
        self.login_button = (By.ID, "login-button")
        self.login_error = (By.XPATH, "//h3[@data-test='error']")
        self.add_cart_1 = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_icon = (By.XPATH, "//span[@class='shopping_cart_badge']")
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.logout_link = (By.ID, "logout_sidebar_link")

    def login(self, username, password):
        username_input = self.wait.until(EC.visibility_of_element_located(self.username_field))
        username_input.clear()
        username_input.send_keys(username)

        password_input = self.wait.until(EC.visibility_of_element_located(self.password_field))
        password_input.clear()
        password_input.send_keys(password)

        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()
        return self

    def get_login_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.login_error)).text

    def add_product_to_cart(self):
        product = self.wait.until(EC.element_to_be_clickable(self.add_cart_1))
        product.click()
        return self.get_cart_count()

    def get_cart_count(self):
        cart_badge = self.wait.until(EC.visibility_of_element_located(self.cart_icon))
        return int(cart_badge.text) if cart_badge.text else 0

    def logout(self):
        menu_button = self.wait.until(EC.element_to_be_clickable(self.menu_button))
        menu_button.click()

        logout_button = self.wait.until(EC.element_to_be_clickable(self.logout_link))
        logout_button.click()
        return self

    def relogin(self, username, password):
        self.login(username, password)
        first_cart_count = self.add_product_to_cart()

        self.logout()
        self.login(username, password)
        second_cart_count = self.get_cart_count()

        assert first_cart_count == second_cart_count
        return first_cart_count, second_cart_count
    


# Backward compatible alias for the older test imports.
login_details = LoginPage

