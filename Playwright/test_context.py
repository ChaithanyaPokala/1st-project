import pytest
from playwright.sync_api import sync_playwright,expect,Playwright
def test_browser_context(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page1=context.new_page()
    page2=context.new_page()
    page1.goto("https://testautomationpractice.blogspot.com/")
    page1.locator("#name").fill("chaitanya")
    expect(page1).to_have_url("https://testautomationpractice.blogspot.com/")
    page2.goto("https://automationexercise.com/")
    page2.locator("body > section:nth-child(3) > div > div > div.col-sm-9.padding-right > div.features_items > div:nth-child(3) > div > div.single-products > div.productinfo.text-center > a")

