import pytest
from playwright.sync_api import sync_playwright,expect,Page
def test_mouse_actions(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    point_me=page.get_by_text(text="Point Me")
    point_me.hover()
    laptops=page.locator(".dropdown-content a:nth-child(2)")
    laptops.hover()
    # right_click=page.get_by_text(text="Copy Text")
    # right_click.click(button="right")
    double_click=page.get_by_text(text="Copy Text")
    double_click.dblclick()
