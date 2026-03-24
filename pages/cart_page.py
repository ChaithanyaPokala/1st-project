from playwright.sync_api import Page
from selenium.webdriver.support.expected_conditions import none_of


class CartPage:
    def __init__(self,page):
        self.page=page
        #products list added in cart
        self.product_name_locator=self.page.locator("div .table-responsive tbody tr td:nth-child(2)")

    def products_name(self,productname):
        products=self.product_name_locator
        count=products.count()
        for i in range(count):
            name=products.nth(i).inner_text()
            if name==productname:
                return products.nth(i)

        return None
