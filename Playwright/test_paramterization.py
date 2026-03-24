import pytest
from playwright.sync_api import sync_playwright,expect,Page
search_items=('laptop','smartphone','giftcard','monitor')
@pytest.mark.parametrize("item", search_items)
def test_parameterization(item,page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("#small-searchterms").fill(item)
    page.locator("input[type=submit]").click()