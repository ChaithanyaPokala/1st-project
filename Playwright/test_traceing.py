import pytest
from playwright.sync_api import sync_playwright,expect,Playwright
def test_tracing(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    context.tracing.start(screenshots=True,snapshots=True)
    page=context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("#male").check()
    context.tracing.stop(path="trace.zip")