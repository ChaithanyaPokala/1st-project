import pytest
import datetime
from playwright.sync_api import sync_playwright,expect,Page
def test_screenshot(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    timestamp=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    # page.screenshot(path=f"screenshots/homepage-{timestamp}.png")
    # page.screenshot(path=f"screenshots/fullpage-{timestamp}.png",full_page=True)
    # logo=page.locator("#Blog1 > div.blog-posts.hfeed > div > div > div > div > h3 > a")
    # logo.screenshot(path=f"screenshots/logo-{timestamp}.png")
