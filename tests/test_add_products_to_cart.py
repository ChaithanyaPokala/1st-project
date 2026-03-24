import pytest
from playwright.sync_api import Page,expect
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage

#
# @pytest.mark.parametrize("username,password,productname",[
#     ("chaithanyatest","test@123","Samsung galaxy s6")
# ])
def test_user_can_login_and_add_products_to_cart(page:Page):
    page.goto("https://www.demoblaze.com/")
    login_page=LoginPage(page)
    login_page.perform_login(username='chaithanyatest', password='test@123')
    home_page=HomePage(page)
    home_page.add_products_list("Samsung galaxy s6")
    home_page.go_to_cart()
    cart_page=CartPage(page)
    product_in_cart=cart_page.products_name("Samsung galaxy s6")

    # Assertion
    expect(product_in_cart).to_be_visible()

