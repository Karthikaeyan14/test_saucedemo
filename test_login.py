import json
from pathlib import Path

import pytest

from PageObjectMode.admin_details import admin
from PageObjectMode.login_details import LoginPage

DATA_FILE = Path(__file__).parent / "json" / "test_correctlogindetails.json"

with DATA_FILE.open() as data_file:
    test_data = json.load(data_file)

valid_login_data = test_data["data"]
invalid_login_data = test_data["wrong_data"]


@pytest.mark.parametrize("test_item_data", valid_login_data)
@pytest.mark.regression
def test_saucedemo(broswerInstance, test_item_data):
    """Verify that a valid login flow reaches the product checkout flow."""
    driver = broswerInstance
    login_page = LoginPage(driver)
    login_page.login(test_item_data["user_name"], test_item_data["password"])

    product = admin(driver)
    product.method()
    product.checkout()
    product.processed()


@pytest.mark.parametrize("login_data", invalid_login_data)
@pytest.mark.smoke
def test_invalid_login(broswerInstance, login_data):
    """Verify that invalid credentials display a login error."""
    login_page = LoginPage(broswerInstance)
    login_page.login(login_data["user_name"], login_data["password"])
    error_message = login_page.get_login_error_message()
    assert error_message == (
        "Epic sadface: Username and password do not match any user in this service"
    )


@pytest.mark.smoke
def test_empty_login(broswerInstance):
    """Verify that an empty username triggers the correct validation message."""
    login_page = LoginPage(broswerInstance)
    login_page.login("", "")
    error_message = login_page.get_login_error_message()
    assert error_message == "Epic sadface: Username is required"


@pytest.mark.smoke
def test_empty_password(broswerInstance):
    """Verify that an empty password triggers the correct validation message."""
    login_page = LoginPage(broswerInstance)
    login_page.login("standard_user", "")
    error_message = login_page.get_login_error_message()
    assert error_message == "Epic sadface: Password is required"


@pytest.mark.relogin
def test_relogin(broswerInstance):
    """Verify that the cart count remains the same after logout and login again."""
    login_page = LoginPage(broswerInstance)
    first_cart_count, second_cart_count = login_page.relogin("standard_user", "secret_sauce")
    assert first_cart_count == second_cart_count


@pytest.mark.relogin
def test_customer_not_update(broswerInstance):
    """Verify that the cart count remains the same after logout and login again."""
    driver = broswerInstance
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    
    product = admin(driver)
    product.method()
    product.customer_detail()
    
    assert product.error_message() == "Error: First Name is required"

@pytest.mark.remove_product
def test_remove_product_from_cart(broswerInstance):
    """Verify that the cart count decreases after removing a product from the cart."""
    driver = broswerInstance
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    
    product = admin(driver)
    product.method()
    
    initial_cart_count = product.get_cart_count()
    product.remove_product_from_cart()
    updated_cart_count = product.get_cart_count()
    
    assert updated_cart_count == initial_cart_count - 1