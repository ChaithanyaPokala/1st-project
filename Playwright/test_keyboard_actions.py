import pytest
from playwright.sync_api import sync_playwright,expect,Page
def test_keyword_action(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    input=page.locator("#input1")
    input.focus()
    page.keyboard.insert_text("Chaitanya")
    page.keyboard.press("Control+A")
    page.keyboard.press("Control+C")
    page.keyboard.press("Tab")
    page.keyboard.press("Control+V")
    page.keyboard.press("Tab")
    page.keyboard.press("Control+V")

