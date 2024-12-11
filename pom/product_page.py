from playwright.sync_api import Page

class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_item_to_cart = ".btn.btn-default.add-to-cart"
        self.products = ".col-sm-4"
        self.added_product_text = "Your product has been added to cart."
        self.continue_shopping = ".btn.btn-success.close-modal.btn-block"


    def navigate_to_product_page(self, base_url):
        if base_url.endswith("/"):
            self.page.goto(base_url + "products")
        else:
            self.page.goto(base_url + "/products")


    def add_to_cart(self,product):
        product.locator(self.add_item_to_cart).first.click()


    def get_products_less_than_price(self, price):
        products = self.page.locator(".features_items").locator(self.products)
        products_count = products.count()

        for i in range(products_count):
            product = products.nth(i)
            product_price = int(self.extract_product_price(product))

            if product_price <= price:
                self.add_to_cart(product)

                if not self.is_product_added_to_cart():
                    raise Exception(f"Product with relevant price of: {product_price} has not been added to the cart")

                self.page.locator(self.continue_shopping).click()


    def is_product_added_to_cart(self):
        return self.page.is_visible(f"text={self.added_product_text}")

    def extract_product_price(self, product):
        product_price_with_currency = product.locator("div.productinfo.text-center > h2").inner_text()
        return product_price_with_currency.split()[1]