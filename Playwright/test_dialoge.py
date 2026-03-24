import pytest
from playwright.sync_api import sync_playwright,expect,Page
def test_dialoge(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    # page.locator("#alertBtn").click()
    # page.on("dialog",lambda dialog:dialog.accept())
    # page.locator("#confirmBtn").click()
    # page.on("dialog",lambda dialog:dialog.dismiss())
    # page.wait_for_timeout(5000)
    page.locator("#promptBtn").click()
    page.on("dialog",lambda dialog:dialog.accept("john"))
    text=page.locator("//*[@id='demo']")
    page.wait_for_timeout(5000)
    expect(text).to_have_text("User cancelled the prompt.")