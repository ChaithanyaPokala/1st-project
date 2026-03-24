import pytest
from playwright.sync_api import sync_playwright,expect,Page
def test_dynamic_webtable(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    table=page.locator("table[id='taskTable']")
    rows=table.locator('tr').all()
    print(rows)
    cpu=""
    for row in rows:
        process_name=row.locator("td").nth(0).inner_text()
        page.wait_for_timeout(5000)
        if process_name=="Chrome":
            cpu=row.locator("td:has-text('%')").inner_text()
            print(cpu)
            break

    page.wait_for_timeout(5000)




