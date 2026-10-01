import json
from pathlib import Path

import pytest

from PageObjectMode.admin_details import admin
from PageObjectMode.login_details import LoginPage


import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


DATA_FILE = Path(__file__).parent / "json" / "test_correctlogindetails.json"

with DATA_FILE.open() as data_file:
    test_data = json.load(data_file)

valid_login_data = test_data["data"][0]
invalid_login_data = test_data["wrong_data"]
customer=test_data['Customer_details'][0]


@pytest.mark.parametrize(
    "test_item_data",
    [(valid_login_data)]
)
@pytest.mark.relogin
def test_customer_not_update(broswerInstance,test_item_data):
    """Verify that the cart count remains the same after logout and login again."""
    driver = broswerInstance
    login_page = LoginPage(driver)
    login_page.login(test_item_data["user_name"], test_item_data["password"])
    
    product = admin(driver)
    product.method()
    product.cart_details()
    #product.checkout(customer_data["first_name"],customer_data['last_name'],customer_data['pincode'])
    
    product.checkout("","","")
    assert product.error_message() == "Error: First Name is required"
    logging.info("Error message is:", product.error_message())

@pytest.mark.parametrize(
    "test_item_data",
    [(valid_login_data)]
)
@pytest.mark.relogin
def test_customer_lastname_not_update(broswerInstance,test_item_data):
    """Verify that the cart count remains the same after logout and login again."""
    driver = broswerInstance
    login_page = LoginPage(driver)
    login_page.login(test_item_data["user_name"], test_item_data["password"])
            
    product = admin(driver)
    product.method()
    product.cart_details()

    product.checkout('karthi',"","")
    
    assert product.error_message() == "Error: Last Name is required"
    logging.info("Error message is:", product.error_message())

@pytest.mark.parametrize("test_item_data, customer_details",[(valid_login_data, customer)])
@pytest.mark.cost_details
def test_cost(broswerInstance,test_item_data,customer_details):
    '''Verify that the product cost is displayed correctly in the cart'''
    driver=broswerInstance
    login_page = LoginPage(driver)
    login_page.login(test_item_data["user_name"], test_item_data["password"])
        
    product = admin(driver)
    product.method()
    product.price_details()
    product.cart_details()
    product.checkout(customer_details['first_name'],customer_details['last_name'],customer_details['pincode'])
    product.summary_total()
    product.processed()
 


@pytest.mark.specific_product    
@pytest.mark.parametrize(
    "test_item_data",
    [(valid_login_data)]
)
def test_specific_product_removal(broswerInstance,test_item_data):
    """Verify that a specific product can be removed from the cart and the cart count decrements."""
    driver = broswerInstance
    login_page = LoginPage(driver)
    login_page.login(test_item_data["user_name"], test_item_data["password"])    
    product = admin(driver)
    product.method()
    
    initial_cart_count = product.get_cart_count()
    logging.info("Initial cart count:", initial_cart_count)
    
    # Remove a specific product from the cart
    product.remove_specific_product_from_cart("Sauce Labs Onesie")
    
    updated_cart_count = product.get_cart_count()
    logging.info("Updated cart count after removal:", updated_cart_count)
    
    assert updated_cart_count == initial_cart_count - 1
    
@pytest.mark.remove_product

@pytest.mark.parametrize(
    "test_item_data",
    [(valid_login_data)]
)
def test_remove_product_from_cart(broswerInstance,test_item_data):
    #Verify that the cart count decreases after removing a product from the cart.
    driver = broswerInstance
    login_page = LoginPage(driver)
    login_page.login(test_item_data["user_name"], test_item_data["password"])

    
    product = admin(driver)
    product.method()
    
    initial_cart_count = product.get_cart_count()
    product.remove_product_from_cart()
    #assert product.get_cart_count() == 0
    #updated_cart_count = product.get_cart_count()
    
    #assert updated_cart_count == initial_cart_count - 1"""
