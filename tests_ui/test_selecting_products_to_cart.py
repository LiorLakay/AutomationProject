from pom.login_page import LoginPage
from config import CONFIG
import pytest

from pom.product_page import ProductPage


def test_selecting_product_under_given_price(browser_context):
    try:
        # Creating relevant page objects
        login_page = LoginPage(browser_context)
        product_page = ProductPage(browser_context)

        # Logging in the user
        login_page.login_user(CONFIG["new_user"]["email"], CONFIG["new_user"]["password"])
        if not login_page.is_login_successful():
            raise Exception("Test failed due to login error")

        # Selecting the relevant price products to cart
        product_page.navigate_to_product_page(CONFIG["app_url"])
        product_page.get_products_less_than_price(600)  # Can provide arbitrary price

    except Exception as e:
        pytest.fail(f"Test failed: {e}")