import json
from pathlib import Path

import pytest

from PageObjectMode.admin_details import admin
from PageObjectMode.login_details import LoginPage

DATA_FILE = Path(__file__).parent / "json" / "test_correctlogindetails.json"

with DATA_FILE.open() as data_file:
    test_data = json.load(data_file)

valid_login_data = test_data["data"]

@pytest.mark.relogin
def test_customer_not_update(broswerInstance):
    """Verify that the cart count remains the same after logout and login again."""
    driver = broswerInstance
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    
    product = admin(driver)
    product.method()
    product.cart_details()
    product.checkout("","","")
    
    assert product.error_message() == "Error: First Name is required"
    print("Error message is:", product.error_message())

@pytest.mark.relogin

def test_customer_lastname_not_update(broswerInstance):
    """Verify that the cart count remains the same after logout and login again."""
    driver = broswerInstance
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    
    product = admin(driver)
    product.method()
    product.cart_details()

    product.checkout('karthi',"","")
    
    assert product.error_message() == "Error: Last Name is required"
    print("Error message is:", product.error_message())

@pytest.mark.cost_details
def test_cost(broswerInstance):
    '''Verify that the product cost is displayed correctly in the cart'''
    driver=broswerInstance
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    product = admin(driver)
    product.method()
    product.price_details()
    product.cart_details()
    product.checkout('karthi','r','613001')
    product.summary_total()
    product.processed()
 
 
@pytest.mark.specific_product    
def test_specific_product_removal(broswerInstance):
    """Verify that a specific product can be removed from the cart and the cart count decrements."""
    driver = broswerInstance
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    
    product = admin(driver)
    product.method()
    
    initial_cart_count = product.get_cart_count()
    print("Initial cart count:", initial_cart_count)
    
    # Remove a specific product from the cart
    product.remove_specific_product_from_cart("Sauce Labs Backpack")
    
    updated_cart_count = product.get_cart_count()
    print("Updated cart count after removal:", updated_cart_count)
    
    assert updated_cart_count == initial_cart_count - 1