from playwright.sync_api import Page
class HomePage:
    def __init__(self, page):
        self.page = page
        self.add_products_list_locator=self.page.locator("#tbodyid .card-title a")
        self.add_to_cart_button_locator=self.page.locator(".btn btn-success btn-lg")
        self.go_to_cart_locator=self.page.locator("#cartur")

    #Actions
    def add_products_list(self,product_name):
        products=self.add_products_list_locator
        count=products.count()

        for i in range(count):
            name=products.nth(i).innerText()
            if name==product_name:
                products.nth(i).click()
                break
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.add_to_cart_button_locator.click()

    def go_to_cart(self):
        self.go_to_cart_locator.click()



