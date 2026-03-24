import pytest
from playwright.sync_api import sync_playwright,expect,Playwright,Page
def test_tabs(playwright: Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")
    page.get_by_text(text="New Tab").click()
    page.wait_for_timeout(5000)
    all_pages=context.pages
    print(len(all_pages))

    childpage=all_pages[1]
    expect(childpage.locator("#header-inner > div.titlewrapper > h1")).to_have_text("SDET-QA Blog")
