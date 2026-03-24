import pytest
from playwright.sync_api import sync_playwright,expect,Page
def test_pagenation(page:Page):
    page.goto("https://practice.expandtesting.com/dynamic-pagination-table")
    has_more_pages=True
    table=page.locator("#example")
    rows=table.locator("#example tbody tr").all()
    page.wait_for_timeout(5000)
    print(rows)
    next_button=page.locator("//*[@id='example_next']")
    is_disabled=next_button.get_attribute("class")
    if 'disabled' in is_disabled:
        has_more_pages=False
    else:
        next_button.click()
    page.wait_for_timeout(5000)