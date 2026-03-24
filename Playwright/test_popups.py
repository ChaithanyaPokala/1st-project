import pytest
from playwright.sync_api import sync_playwright,expect,Playwright
def test_popups(playwright:Playwright):
    browser=playwright.chromium.launch(headless=True)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("#PopUp").click()
    all_pages=context.pages
    count=len(all_pages)
    print("lenghth of pahes",count)
    for pw in all_pages:
        URL=pw.url
        title=pw.title
        print("URL",URL)
        print("title",title)
        if "Playwright" in URL:
            pw.locator(".getStarted_Sjon").click()
            expect(pw).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright Python")