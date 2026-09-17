import pytest
from PageObjectMode.login_details import login_details
from PageObjectMode.admin_details import admin
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "json" / "test_correctlogindetails.json"

with DATA_FILE.open() as data_file:
    test_data = json.load(data_file)

valid_login_data = test_data["data"]
invalid_login_data = test_data["wrong_data"]


@pytest.mark.parametrize("test_item_data", valid_login_data)
@pytest.mark.regression
def test_saucedemo(broswerInstance,test_item_data):
    #Correct login details
    driver=broswerInstance
    enter_login=login_details(driver)
    enter_login.enter_login_details(test_item_data['user_name'], test_item_data['password'])
    
    product=admin(driver)
    product.method()
    product.checkout()
    product.processed()

@pytest.mark.parametrize("login_data", invalid_login_data)
@pytest.mark.smoke
def test_invalid_login(broswerInstance, login_data):
    """Verify that invalid credentials display a login error."""
    login_page = login_details(broswerInstance)
    login_page.enter_login_details(login_data["user_name"], login_data["password"])
    error_message = login_page.login_error_message()
    assert error_message == (
        "Epic sadface: Username and password do not match any user in this service"
    )
    print("Error message is:", error_message)
    

@pytest.mark.smoke
def test_empty_login(broswerInstance):
    #verify that empty credentials display a login error.
    login_page = login_details(broswerInstance)
    login_page.enter_login_details("", "")
    error_message = login_page.login_error_message()
    assert error_message == "Epic sadface: Username is required"
    print("Error message is:", error_message)
    
@pytest.mark.smoke
def test_empty_password(broswerInstance):
    #verify that empty password display a login error.
    login_page = login_details(broswerInstance)
    login_page.enter_login_details("standard_user", "")
    error_message = login_page.login_error_message()
    assert error_message == "Epic sadface: Password is required"
    print("Error message is:", error_message)