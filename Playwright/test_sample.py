# import pytest
from playwright.sync_api import Page,expect
def test_verifypageurl(page:Page):
    page.goto("https://demo.nopcommerce.com/")
    myurl=page.url
    expect(page).to_have_url(myurl)
    page.get_by_placeholder("Search store").fill("Apple")
    page.locator("//*[@id='small-search-box-form']/button").click()
