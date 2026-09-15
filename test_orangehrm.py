import pytest
from PageObjectMode.login import login_details
from PageObjectMode.admin import admin

def test_saucedemo(broswerInstance):
    driver=broswerInstance
    enter_login=login_details(driver)
    enter_login.enter_login_details('standard_user', 'secret_sauce')
    product=admin(driver)
    product.method()
    product.checkout()
    product.processed()

@pytest.mark.smoke()
#User Allow to enter the wrong password
def test_saucedemo1(broswerInstance):
    driver=broswerInstance
    enter_login=login_details(driver)
    enter_login.enter_login_details('##', '12')
                                    